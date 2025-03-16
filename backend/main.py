from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.summarization import text_summary
import uvicorn

app = FastAPI(title="Text Summarization API", description="Text Summarization API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text_summary)