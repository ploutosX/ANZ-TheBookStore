from . import schemas, models
from datetime import datetime, date
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import tuple_
from typing import List
from uuid import uuid4


def get_books_by_category_and_or_theme(db: Session, category: str, theme: str):
    if category and theme:
        return db.query(models.Book).filter(
            models.Book.category == category,
            models.Book.theme == theme).all()
    elif category:
        return db.query(models.Book).filter(
            models.Book.category == category).all()
    elif theme:
        return db.query(models.Book).filter(
            models.Book.theme == theme).all()
    else:
        return db.query(models.Book).all()


def search_books_by_title_or_author(db: Session, search: str):
    return db.query(models.Book).filter(
        models.Book.name.ilike(f"%{search}%") | models.Book.author.ilike(f"%{search}%")).all()


def create_or_modify_books(db: Session, books: List[schemas.BookBase]):
    values = [(books.name, books.author, books.year, books.category,
               books.theme, books.version) for books in books]

    existing_books = db.query(models.Book).filter(
        tuple_(models.Book.name, models.Book.author, models.Book.year,
               models.Book.category, models.Book.theme, models.Book.version).in_(values)).all()

    for book in books:
        if book in existing_books:
            # Update the existing book
            existing_book = db.query(models.Book).filter(
                models.Book.name == book.name,
                models.Book.author == book.author,
                models.Book.year == book.year,
                models.Book.category == book.category,
                models.Book.theme == book.theme,
                models.Book.version == book.version
            ).first()

            existing_book.genre = book.genre
            existing_book.price = book.price
            existing_book.discount = book.discount
            existing_book.stock = book.stock
            existing_book.description = book.description
            existing_book.image = book.image
            existing_book.active = book.active
        else:
            # Create a new book
            new_book = models.Book(
                id=uuid4(),
                name=book.name,
                author=book.author,
                year=book.year,
                category=book.category,
                theme=book.theme,
                version=book.version,
                genre=book.genre,
                price=book.price,
                discount=book.discount,
                stock=book.stock,
                description=book.description,
                image=book.image,
                active=book.active
            )
            db.add(new_book)
    db.commit()
    return books


def search_books_by_category(db: Session, category: str):
    return db.query(models.Book).filter(
        models.Book.category == category).all()
