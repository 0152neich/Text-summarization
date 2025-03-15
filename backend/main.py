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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", workers=1, port=8000, reload=True)