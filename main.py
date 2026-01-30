from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

from src.routes.query import router as query

load_dotenv()

app = FastAPI()

app.include_router(query, prefix = "/api", tags = ['query'])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  
    )
