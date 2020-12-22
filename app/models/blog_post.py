from pydantic import BaseModel
from typing import Optional

class BlogPost(BaseModel):
    id: Optional[int] = 0
    title: Optional[str] = None
    author: Optional[str] = None