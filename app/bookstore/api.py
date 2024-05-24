from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from enum import Enum
from . import crud, schemas
from typing import List


router = APIRouter(prefix="/bookstore", tags=["Book Store"])


class Category(str, Enum):
    fiction = "fiction"
    non_fiction = "non-fiction"
    fantasy = "fantasy"
    mystery = "mystery"
    thriller = "thriller"
    romance = "romance"
    horror = "horror"
    science_fiction = "science fiction"
    historical_fiction = "historical fiction"
    poetry = "poetry"
    drama = "drama"
    young_adult = "young adult"
    children = "children"
    biography = "biography"
    autobiography = "autobiography"
    memoir = "memoir"
    self_help = "self-help"
    health = "health"
    history = "history"
    travel = "travel"
    guide = "guide"
    cook = "cook"
    art = "art"
    photography = "photography"
    science = "science"
    nature = "nature"
    technology = "technology"
    computer = "computer"
    programming = "programming"
    business = "business"
    finance = "finance"
    marketing = "marketing"
    management = "management"
    leadership = "leadership"
    entrepreneurship = "entrepreneurship"
    economics = "economics"
    politics = "politics"
    religion = "religion"
    philosophy = "philosophy"
    psychology = "psychology"
    sociology = "sociology"
    anthropology = "anthropology"
    archaeology = "archaeology"
    education = "education"
    law = "law"
    library = "library"
    information = "information"
    sports = "sports"
    games = "games"
    music = "music"
    film = "film"
    television = "television"
    theatre = "theatre"
    dance = "dance"
    opera = "opera"
    architecture = "architecture"
    design = "design"
    fashion = "fashion"
    beauty = "beauty"
    fitness = "fitness"
    diet = "diet"
    nutrition = "nutrition"
    parenting = "parenting"
    family = "family"
    relationship = "relationship"


class Theme(str, Enum):
    action = "action"
    adventure = "adventure"
    comedy = "comedy"
    drama = "drama"
    fantasy = "fantasy"
    historical = "historical"
    horror = "horror"
    mystery = "mystery"
    romance = "romance"
    science_fiction = "science fiction"
    thriller = "thriller"
    crime = "crime"
    detective = "detective"
    espionage = "espionage"
    legal = "legal"
    medical = "medical"
    political = "political"
    psychological = "psychological"
    spy = "spy"
    supernatural = "supernatural"
    western = "western"
    animation = "animation"
    children = "children"
    family = "family"
    musical = "musical"
    science = "science"
    fiction = "fiction"
    non_fiction = "non-fiction"
    self_help = "self-help"
    health = "health"
    history = "history"
    travel = "travel"
    guide = "guide"
    cook = "cook"
    art = "art"
    photography = "photography"
    nature = "nature"
    technology = "technology"
    computer = "computer"
    programming = "programming"
    business = "business"
    finance = "finance"
    marketing = "marketing"
    management = "management"
    leadership = "leadership"
    entrepreneurship = "entrepreneurship"
    economics = "economics"
    politics = "politics"
    religion = "religion"
    philosophy = "philosophy"
    psychology = "psychology"
    sociology = "sociology"
    anthropology = "anthropology"
    archaeology = "archaeology"
    education = "education"
    law = "law"
    library = "library"
    information = "information"
    sports = "sports"
    games = "games"
    music = "music"
    film = "film"
    television = "television"
    theatre = "theatre"
    dance = "dance"
    opera = "opera"
    architecture = "architecture"
    design = "design"
    fashion = "fashion"
    beauty = "beauty"
    fitness = "fitness"
    diet = "diet"
    nutrition = "nutrition"


@router.get("/ListBooks", response_model=List[schemas.BookBase])
def get_books_by_catergory_or_theme(category: Category = None, theme: Theme = None, db: Session = Depends(get_db)):
    """
    Retrieve books by category and/or theme
    """
    return crud.get_books_by_category_and_or_theme(db, category, theme)


@router.post("/SearchBooksByTitleOrAuthor", response_model=List[schemas.BookBase])
def search_books_by_title_or_author(search: str, db: Session = Depends(get_db)):
    """
    Search books by title or author
    """
    return crud.search_books_by_title_or_author(db, search)


@router.post("/CreateOrModifyBooks", response_model=List[schemas.BookBase])
def create_or_modify_books(books: List[schemas.BookBase], db: Session = Depends(get_db)):
    """
    Create or modify books
    """
    return crud.create_or_modify_books(db, books)


@router.get("/SeachBooksByCategory", response_model=List[schemas.BookBase])
def search_books_by_category(category: Category, db: Session = Depends(get_db)):
    """
    Search books by category
    """
    return crud.search_books_by_category(db, category)
