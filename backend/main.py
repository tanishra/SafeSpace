from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import news

app = FastAPI(title="SafeSpace Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news.router)