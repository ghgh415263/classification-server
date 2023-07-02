from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True)
    analysis_model_id = Column(Integer, nullable=False)
    store_filename = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class AnalysisModel(Base):
    __tablename__ = "analysis_model"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    path = Column(Text, nullable=False)
    class_list = Column(Text, nullable=True)
    create_date = Column(DateTime, nullable=False)