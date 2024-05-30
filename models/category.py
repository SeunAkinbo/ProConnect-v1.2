#!/usr/bin/python3
"""category Module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """
    Category class
    Inherits from BaseModel and Base
    """
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    profile = relationship("Profile", back_populates="category", uselist=False)
