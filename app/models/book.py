# models/book.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from app.db import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), ForeignKey("users.user_id"), nullable=False)
    book_information_id = Column(Integer, ForeignKey("book_informations.book_information_id"), nullable=False)
    donation_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="books")
    book_information = relationship("BookInformation", back_populates="books")
    book_requests = relationship("BookRequest", back_populates="book")
    book_loans = relationship("BookLoan", back_populates="book")