from fastapi import FastAPI
from .routers import blog_posts

app = FastAPI()
app.include_router(blog_posts.router)
