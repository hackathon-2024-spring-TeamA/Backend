# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    nickname = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    updated_by = Column(Integer)
    is_delete = Column(Boolean, nullable=False, default=False)

    books = relationship("Book", back_populates="user")
    book_requests = relationship("BookRequest", foreign_keys="[BookRequest.requester_id, BookRequest.holder_id]", back_populates="user")
    book_loans = relationship("BookLoan", back_populates="user")