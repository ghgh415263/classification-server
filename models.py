from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True)
    store_filename = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True)
    path = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)