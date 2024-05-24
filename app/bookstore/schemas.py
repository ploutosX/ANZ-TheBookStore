from datetime import datetime
from enum import Enum
from pydantic import BaseModel, field_validator
from typing import Optional


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


class BookBase(BaseModel):
    name: str
    author: str
    year: int
    category: Category
    theme: Theme
    version: str
    genre: Optional[str]
    price: Optional[int]
    discount: Optional[float]
    stock: Optional[int]
    description: Optional[str]
    image: Optional[str]
    active: bool

    @field_validator(
        "name",
        "author",
        "category",
        "theme",
        "version",
        mode="before",
    )
    def check_empty(cls, value, field):
        if value.strip() == "" or value is None:
            raise ValueError(f"{field} cannot be empty.")
        return value.strip()

    @field_validator(
        "year",
        mode="before"
    )
    def check_year(cls, value):
        if value < 0 or value > datetime.now().year:
            raise ValueError("Invalid year.")
        return value

    @field_validator(
        "price",
        mode="before")
    def check_price(cls, value):
        if value < 0 or not isinstance(value, (int, float)):
            raise ValueError("Invalid price.")
        return int(value)

    @field_validator(
        "discount",
        mode="before")
    def check_discount(cls, value):
        if not value or value == '':
            return None
        if value < 0 or value > 100 or not isinstance(value, (int, float)):
            raise ValueError("Invalid discount.")
        return float(value)

    @field_validator(
        "stock",
        mode="before")
    def check_stock(cls, value):
        if not value or value == '':
            return None
        if value < 0 or not isinstance(value, int):
            raise ValueError("Invalid stock.")
        return int(value)

    @field_validator(
        "active",
        mode="before")
    def check_active(cls, value):
        if value not in [True, False]:
            raise ValueError("Invalid active value.")
        return value
