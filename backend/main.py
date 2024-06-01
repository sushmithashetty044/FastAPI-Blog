from fastapi import FastAPI
from core.config import settings
app=FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VESRION)

@app.get("/")
def hello():
    return {"msg":"Hello FASTAPI"}

