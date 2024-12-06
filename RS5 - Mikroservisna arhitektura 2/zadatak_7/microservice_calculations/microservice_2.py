from aiohttp import web

{
"podaci" : [1,2,3,4,5,6,7,8,9,10]
}


async def handle_umnozak(request):
    data = await request.json()
    data_brojevi = data.get("podaci")
    if not data_brojevi:
        return web.json_response({"error:": "Brojevi nisu proslijeđeni."}, status=400)
    umnozak = 1
    for broj in data_brojevi:
        umnozak*=broj
    return web.json_response({"umnozak": umnozak})

app = web.Application()
app.router.add_post('/umnozak', handle_umnozak)

if __name__ == "__main__":
    web.run_app(app, port=8084)