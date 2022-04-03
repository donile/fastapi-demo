from fastapi import FastAPI
from .models.book import Book

books = []

app = FastAPI()


@app.get("/books")
def get_books():
    return [
        { "Title": "Chamber of Secrets", "Author": "J.K. Rowling" },
        { "Title": "Assassin's Apprentice", "Author": "Robin Hobb" }
    ]

@app.post("/books", status_code=201)
def post_book(book: Book):
    books.append(book)
    return
