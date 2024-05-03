# models/book_information.py
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from app.db import Base

class BookInformation(Base):
    __tablename__ = "book_informations"

    book_information_id = Column(Integer, primary_key=True)
    isbn_number = Column(String(13), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    published_date = Column(Date)
    description = Column(Text)
    image_path = Column(String(255))

    books = relationship("Book", back_populates="book_information")