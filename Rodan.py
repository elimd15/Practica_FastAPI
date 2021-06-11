from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    add = "add"
    update = "update"
    delete = "delete"

app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName, key: str = None):
    if model_name == ModelName.add:
        return {"model_name": model_name, "message": "¡Esta es una operación de adición!", "key": key}
    if model_name.value == "update":
        return {"model_name": model_name, "message": "¡Esta es una operación de actualización!", "key": key}
    return {"model_name": model_name, "message": "¡Esta es una operación de eliminación!", "key": key}

