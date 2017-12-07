import async_timeout
import os

import aiohttp
import aiohttp.web


UPSTREAM_HOST = os.environ['UPSTREAM_HOST']
URL = 'http://%s:8080' % UPSTREAM_HOST
SESSION = aiohttp.ClientSession()


async def handle(request):
    payload = await request.content.read()
    with async_timeout.timeout(30):
        async with SESSION.post(URL, data=payload) as response:
            return aiohttp.web.Response(text=await response.text())

app = aiohttp.web.Application(debug=False)
app.router.add_post('/', handle)

aiohttp.web.run_app(app)
