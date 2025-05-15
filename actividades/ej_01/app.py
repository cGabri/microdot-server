from microdot import Microdot, send_file

app = Microdot()

@app.get('/')
async def index(request):
    return send_file('/index.html')

@app.get('/styles.css')
async def styles(request):
    return send_file('/styles.css')

app.run(port=80)

