from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root(message):
    return {'message':message}

