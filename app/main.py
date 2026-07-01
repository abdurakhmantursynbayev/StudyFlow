from fastapi import FastAPI
from app.core.database import engine
from app.api.auth import router as auth_router
from app.api.course import router as course_router
from app.api.enrollment import router as enollment_router
from app.api.user import router as user_router



app = FastAPI(title="StudyFlow", description="Online course platform", version="1.0.0")

app.include_router(auth_router)
app.include_router(course_router)
app.include_router(enollment_router)
app.include_router(user_router)


@app.get("/")
def root():
    
    return {"message": "StudyFlow API",
            "version": "1.0.0"
        }