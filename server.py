import configparser
import sys

from aiohttp import ClientSession, web

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")


async def receive_status(request):
    return web.Response(text=f"Success from {sys.argv[1]}")


async def hello(request):
    for section in CONFIG.sections():
        async with ClientSession() as session:
            url = f"http://{CONFIG[section]['ip']}:{CONFIG[section]['port']}/status"
            async with session.get(url) as resp:
                print(await resp.text())
    return web.Response(text="Hello, world")


def main():
    server_name = sys.argv[1]
    if server_name not in CONFIG:
        raise Exception(f"{server_name} is not on config.ini")

    app = web.Application()
    app.add_routes([web.get("/", hello)])
    app.add_routes([web.get("/status", receive_status)])
    web.run_app(app, port=CONFIG[server_name]["port"], host=CONFIG[server_name]["ip"])


if __name__ == "__main__":
    main()
