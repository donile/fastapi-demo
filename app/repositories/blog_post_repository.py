from typing import List
from ..models.blog_post import BlogPost

blog_posts_db : List[BlogPost] = [
    BlogPost(**{
        "id": 1,
        "title": "Interesting Title",
        "author": "Mark Donile"
    }),
    BlogPost(**{
        "id": 2,
        "title": "Second Title",
        "author": "Eric Ilg"
    })
]