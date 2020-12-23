from fastapi import FastAPI
from .routers import blog_posts
from .routers import token

app = FastAPI()
app.include_router(blog_posts.router)
app.include_router(token.router)
