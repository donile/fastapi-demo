from fastapi import FastAPI

app = FastAPI()


@app.get("/books")
def get_books():
    return [
        { "Title": "Chamber of Secrets", "Author": "J.K. Rowling" },
        { "Title": "Assassin's Apprentice", "Author": "Robin Hobb" }
    ]
