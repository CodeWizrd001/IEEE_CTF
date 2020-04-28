import os
import sys
import asyncio

from sanic import Sanic
from sanic.response import *

app = Sanic("Crawl")

f = open("index.html")
n = f.readlines()
n = ''.join(n)

@app.route("/",methods=["POST","GET"])
def Start(request) :
    return html(n)

async def main():
    try :
        port_ = int(sys.argv[1])
    except IndexError :
        port_ = 10000
    except ValueError :
        print("[!] Invalid Port")
        print("[!] Defaulting To Port 10000")
        port_ = 10000

    sanic_server = await app.create_server(
        host="0.0.0.0", port=port_, return_asyncio_server=True
    )
    sanic_server.after_start()
    try:
        asyncio_server = sanic_server.server
        await asyncio_server.serve_forever()
    finally:
        sanic_server.before_stop()

    await sanic_server.close()

    for connection in sanic_server.connections:
        connection.close_if_idle()
    sanic_server.after_stop()

if __name__ == "__main__" :
    mainCo = main()
    try:
        asyncio.run(mainCo)
    except KeyboardInterrupt:
        print("Keyboard Interrupt Main")
        exit(0)