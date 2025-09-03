from fastapi import FastAPI
from core.routers import pdf_router, llm_router
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI()
app.include_router(llm_router.router)
app.include_router(pdf_router.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app with routers"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}