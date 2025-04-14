from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageResponse(BaseModel):
    message: str

@app.get("/")
async def hello_world():
    return {"message": "Hello World!"} ## We are returning a dictionary (json)

## Use Path Parameters to pass in name
@app.get("/{name}")
async def hello_world_with_me(name: str):
    return {"message": "Hello " + name + "!"}