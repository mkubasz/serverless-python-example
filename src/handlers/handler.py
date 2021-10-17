from fastapi import FastAPI
from mangum import Mangum


app = FastAPI(title="FastAPI")

 
@app.get('/ping')
def pong():
    return {'result': 'pong'}


api = Mangum(app)
