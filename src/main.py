from fastapi import FastAPI
from src.database import Base, engine
from src.auth import models as auth_models
from src.posts import models as post_models
from src.auth.router import router as auth_router
from src.posts.router import router as post_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Project")

# Routers
app.include_router(auth_router)
app.include_router(post_router)
