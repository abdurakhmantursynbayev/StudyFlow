from fastapi import FastAPI
from app.core.database import engine

app = FastAPI(title="StudyFlow", description="Online course platform", version="1.0.0")

@app.get("/")
def root():
    with engine.connect():
        pass
    
    return {"message": "StudyFlow API"}