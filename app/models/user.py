# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(String(36), primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    nickname = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    updated_by = Column(String(36))
    is_delete = Column(Boolean, nullable=False, default=False)
    books = relationship("Book", back_populates="user")
    # 変更: BookRequestとのリレーションシップを2つに分割
    book_requests_as_requester = relationship("BookRequest", foreign_keys="[BookRequest.requester_id]", back_populates="requester")
    book_requests_as_holder = relationship("BookRequest", foreign_keys="[BookRequest.holder_id]", back_populates="holder")
    book_loans = relationship("BookLoan", back_populates="user")