from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

 
@app.get('/')
def pong():
    return {'Ping': 'pong'}


api = Mangum(app)
