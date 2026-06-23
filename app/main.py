from fastapi import FastAPI
from app.core.database import engine

app = FastAPI()

@app.get("/")
def root():
    with engine.connect():
        pass
    
    return {"message": "StudyFlow API"}