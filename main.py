from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title 1', 'author':'Author 1'},
    {'title': 'Title 2', 'author':'Author 2'},
    {'title': 'Title 3', 'author':'Author 3'},
    {'title': 'Title 4', 'author':'Author 4'}
]

@app.get("/books")
async def first_api():
    return BOOKS



@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book



@app.get("/books/")
async def read_cat_by_query(category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold(): 
            books_to_return.append(book)
    return books_to_return




@app.get("/books/{book_author}/")
async def read_author_cat_by_query(book_author: str,category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    
    return books_to_return



