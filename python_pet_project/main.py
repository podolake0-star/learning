from fastapi import FastAPI

app = FastAPI()

@app.get("/request")
def get_my_request():
    return "Hello World"