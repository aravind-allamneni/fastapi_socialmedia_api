from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .routers import post, user, auth, vote
from .database import engine

# models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/users")
app.include_router(post.router, prefix="/posts")
app.include_router(auth.router, prefix="/login")
app.include_router(vote.router, prefix="/vote")


@app.get("/")
async def root():
    return {"message": "Hello World!"}
