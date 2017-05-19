import os
import aiopg
from aiohttp import web


async def init_pg(app):
    conf = app['config']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        loop=app.loop)
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


def init():
    from game.urls import setup_routes
    app = web.Application()
    setup_routes(app)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    return app

app = init()


if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
