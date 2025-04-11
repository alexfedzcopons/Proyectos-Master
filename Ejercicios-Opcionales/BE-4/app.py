from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Book(BaseModel):
        title: str
        author: str
        publish_year: int
        
libros = []

@app.get("/api/books")
def books_list():
        return {"libros":libros}


@app.post("/api/books", status_code= 201)
def create_book(book:Book):
        
        new_book = {
                "Título":book.title,
                "Autor":book.author,
                "Publicación":book.publish_year}
        
        libros.append(new_book)

        return{"message":"Libro Creado",
               "Libro":new_book}