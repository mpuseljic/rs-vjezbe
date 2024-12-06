from aiohttp import web

async def handle_kolicnik(request):
    data = await request.json()
    if 'zbroj' not in data or 'umnozak' not in data:
        return web.json_response({"error:": "Moraju biti zbroj i umnožak"}, status=400)
    
    zbroj = data['zbroj']
    umnozak = data['umnozak']
    
    if zbroj == 0:
        return web.json_response({"error:": "Umnožak se ne može dijeiti s 0"}, status=400)
    
    kolicnik = umnozak/zbroj 
    return web.json_response({"kolicnik": kolicnik})

app = web.Application()
app.router.add_post('/kolicnik', handle_kolicnik)

if __name__ == "__main__":
    web.run_app(app, port=8085)