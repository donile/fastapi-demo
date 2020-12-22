from fastapi import APIRouter, status
from typing import List, Optional
from ..repositories.blog_post_repository import blog_posts_db, BlogPost

router = APIRouter()

@router.get("/blog-posts")
async def blog_posts():
    return blog_posts_db

@router.get("/blog-posts/{id}")
async def get_blog_post_by_id(id: int):
    for bp in blog_posts_db:
        if bp.id == id:
           return bp
    return None

@router.post("/blog-posts", status_code=status.HTTP_201_CREATED)
def add_blog_post(blog_post: BlogPost):
    max_id: int = 0
    for bp in blog_posts_db:
        if bp.id > max_id:
            max_id = bp.id
    blog_post.id = max_id + 1
    blog_posts_db.append(blog_post)
    return blog_post