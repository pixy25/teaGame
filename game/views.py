from aiohttp import web

from game.models import quest


async def index(request):
    return web.Response(text='Hello Aiohttp!')

class Quests(web.View):
    async def get(self):
        return web.json_response(data)

    async def post(self):
        return web.json_response(data)
