from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

#create a dictionary to store books
books = {}

# CRUD Operations
# Create - POST
# Read - GET
# Update - PUT
# Delete - DELETE
book_data = {
    "id": 0,
    "title": "",
    "author": "",
    "year_published": 2000,
    "pages": 0,
    "language": "",
}

@app.get("/")
def home():
    return {"message": "Welcome to the book API"}

#Get all books
@app.get("/books")
def get_books():
    return books

#Create a book
@app.post("/books")
def create_book(
    title: str, author: str, year_published: int, pages: int, language: str
):
    new_book = book_data.copy()
    new_book["id"] = str(UUID(int=len(books) + 1))
    new_book["title"] = title
    new_book["author"] = author
    new_book["year_published"] = year_published
    new_book["pages"] = pages
    new_book["language"] = language

    books[new_book["id"]] = new_book

    return {"message": "Book created succesfully", "data": new_book}

#update a book
@app.put("/books/{id}")
def update_book(
    id: str, title: str, author: str, year_published: int, pages: int, language: str
):
    book = books.get(id)
    if not book:
        return {"errors": "Book not found"}
    
    book["title"] = title
    book["author"] = author
    book["year_published"] = year_published
    book["pages"] = pages
    book["language"] = language

    return {"message": "Book updated successfully", "data": book}

#delete a book
@app.delete("/books{id}")
def delete_book(id: str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    del books[id]

    return{"message": "Book deleted successfully"}
#Get a book by id
@app.get("/books/{id}")
def get_book(id:str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    return {"data": book}