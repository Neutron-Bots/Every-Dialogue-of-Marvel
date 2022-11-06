import json
import logging

import asyncio, aiohttp, logging, traceback
from config import Config

logging.getLogger().setLevel(logging.INFO)

async def ping_server():
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            async with session.get(Config.REPLIT) as resp:
                logging.info(f"Pinged server with response: {resp.status}")
    except TimeoutError:
        logging.warning("Couldn't connect to the site URL..!")
    except Exception:
        traceback.print_exc()

async def getResponse(url, headers=None):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, raise_for_status=True) as response:
            data = await response.json() # get json response data from url
            return data

async def getQoute(url):
    data = await getResponse(url)
    info = data["Items"][0] if "Items" in data else data

    if "id" in info:
        qoute_id = info["id"]
        author = info["data"]["author"]
        quote = info["data"]["quote"]
    elif "_id" in info:
        qoute_id = info["_id"]
        author = info["character"]
        quote = info["quote"]

    with open("log.txt", "r") as f:
        qoute_list = f.read().split(",")
        f.close()

    if qoute_id in qoute_list: # avoid duplicate qoute
        await getQoute(url)
        return

    with open("log.txt", "w") as f: # adding qoute id in log.txt
        qoute_list.append(qoute_id)
        text = " ".join(qoute_list)
        qoute_list = f.write(text)
        f.close()

    return Config.template.format(dialogue=quote, author=author.replace(" ", ""))

# for always run on replit
if Config.REPLIT:
    from threading import Thread

    from flask import Flask, jsonify
    app = Flask('')
    @app.route('/')
    def main():
        res = {
            "status":"running",
            "hosted":"replit.com",
        }
        return jsonify(res)

    def run():
        app.run(host="0.0.0.0", port=8000)
    
    async def keep_alive():
        server = Thread(target=run)
        server.start()