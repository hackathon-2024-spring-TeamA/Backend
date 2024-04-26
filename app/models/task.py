# モデルファイル。テーブルのカラムとリレーションを定義している。

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

# Taskモデルのtaslsテーブル。
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    # doneはDoneモデルとの関係を定義します。これは1対1の関係です。
    # back_populatesは逆方向のリレーションシップを指定し、
    # cascade="delete"はTaskが削除された時に関連するDoneも削除されることを意味します。
    done = relationship("Done", back_populates="task", cascade="delete")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="done")