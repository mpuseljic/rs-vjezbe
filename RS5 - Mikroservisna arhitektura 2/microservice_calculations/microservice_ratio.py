# microservice_ratio.py
import aiohttp
from aiohttp import web
import asyncio

app = web.Application()

{
"podaci": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
"zbroj": 55
}

async def handle_ratio(request):
    data = await request.json()
    data_brojevi = data.get("podaci")
    data_zbroj = data.get("zbroj")
    ratio_list = [round(i / data_zbroj, 2) for i in data_brojevi]
    return web.json_response({"ratio_list": ratio_list})

app.router.add_post('/ratio', handle_ratio)
web.run_app(app, host='localhost', port=8082)