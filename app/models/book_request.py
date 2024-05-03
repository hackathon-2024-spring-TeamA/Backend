# models/book_request.py
from sqlalchemy import Column, Integer, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from app.db import Base

class BookRequest(Base):
    __tablename__ = "book_requests"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    requester_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    holder_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    request_date = Column(Date, nullable=False)
    status = Column(Enum("requested", "sending", "arrived"), nullable=False)
    book = relationship("Book", back_populates="book_requests")
    # 変更: Userとのリレーションシップをrequesterとholderの2つに分割
    requester = relationship("User", foreign_keys=[requester_id], back_populates="book_requests_as_requester")
    holder = relationship("User", foreign_keys=[holder_id], back_populates="book_requests_as_holder")