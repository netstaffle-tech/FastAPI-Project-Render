from fastapi import FastAPI
app = FastAPI()

# CREATE
@app.get("/")
def home():
    return {"status": 200,"message":"Home APi load successfully"}

@app.get("/about")
def home():
    return {"status": 200,"message":"About APi load successfully"}

