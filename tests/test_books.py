from app import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

def test_get_books():
    response = client.get("/books")
    books = response.json()
    assert response.status_code == 200
    assert len(books) == 2
    assert books[0]["Author"] == "J.K. Rowling"

def test_post_book():
    book = {
        "Title": "Learning Python, 5th Edition",
        "Author": "Mark Lutz"
    }
    response = client.post("/books", json=book)
    assert response.status_code == 201
