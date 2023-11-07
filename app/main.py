from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import tensorflow as tf
from tensorflow.keras.models import load_model
from app.code import predict_carsband
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

flowermodel = load_model('model/flower_model.h5')

end_hog = 'http://localhost:8080/api/getpreimg'

@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/flower")
async def read_str(request:Request):
    item = await request.json()
    img = requests.get(end_hog,json=item)
    res = predict_carsband(flowermodel,img.json()['img'])
    return res