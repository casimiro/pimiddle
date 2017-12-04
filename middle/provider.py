import aiohttp
import aiohttp.web


async def handle(request):
    return aiohttp.web.Response(text='{"inserted_id": "asdfasdf"}')

app = aiohttp.web.Application()
app.router.add_post('/', handle)

aiohttp.web.run_app(app)
