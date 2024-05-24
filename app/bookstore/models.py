# Sql Alchemy models for the bookstore app
from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import UniqueConstraint


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    theme = Column(String, nullable=False)
    version = Column(String, nullable=False)
    genre = Column(String)
    price = Column(Integer)
    discount = Column(Float)
    stock = Column(Integer)
    description = Column(String)
    image = Column(String)
    active = Column(Boolean, nullable=False)
    # TO DO: Users, Review and Rating system
    UniqueConstraint('name', 'author', 'year', 'category',
                     'theme', 'version', name='unique_book')
