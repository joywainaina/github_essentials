from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Just completed my github essentials test for 7th November 2025"}