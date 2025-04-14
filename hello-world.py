from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}

## Use Path Parameters to pass in name
@app.get("/{name}")
async def hello_world_with_me(name: str):
    return {"message": "Hello " + name + "!"}