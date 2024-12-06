# microservice_sum.py
from aiohttp import web

{
"podaci" : [1,2,3]
}

async def handle_zbroj(request):
    data = await request.json()
    data_brojevi = data.get("podaci") # ili data['podaci']
    zbroj = sum(data_brojevi)
    return web.json_response({"zbroj": zbroj})

app = web.Application()
app.router.add_post('/zbroj', handle_zbroj)
web.run_app(app, host='localhost', port=8081)