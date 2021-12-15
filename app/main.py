from fastapi import FastAPI

from blog.router import router as blog_router
from users.router import router as users_router
from users import models
from .database import engine


app = FastAPI(
    title="Instagram clone API"
)

app.include_router(blog_router)
app.include_router(users_router)


models.Base.metadata.create_all(engine)
