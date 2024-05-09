# models/book_loan.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.db import Base

class BookLoan(Base):
    __tablename__ = "book_loans"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), ForeignKey("users.user_id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    rent_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date)
    is_held = Column(Boolean, nullable=False, default=True)

    user = relationship("User", back_populates="book_loans")
    book = relationship("Book", back_populates="book_loans")