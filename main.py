from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

MONGO_URI = "mongodb+srv://esp32_proyecto:proyecto123@cluster0.kqtluum.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["proyecto"]     
collection = db["sensor"]   

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

@app.post("/sensor")
def guardar_sensor(data: dict):
    # Agrega la fecha y hora de registro de forma automática al recibir el JSON
    data["fecha"] = datetime.now().isoformat()

    # Guarda el JSON directo en la colección 'sensor'
    collection.insert_one(data)

    return {"status": "dato guardado"}