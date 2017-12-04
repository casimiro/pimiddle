import async_timeout
import os

import aiohttp
import aiohttp.web


UPSTREAM_HOST = os.environ['UPSTREAM_HOST']
URL = 'http://%s:8080' % UPSTREAM_HOST


async def handle(request):
    payload = await request.content.read()
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(30):
            async with session.post(URL, data=payload) as response:
                response_data = await response.text()
                return aiohttp.web.Response(text=response_data)

app = aiohttp.web.Application()
app.router.add_post('/', handle)

aiohttp.web.run_app(app)
