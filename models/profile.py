#!/usr/bin/python3
"""Profile class module"""

from models.base_model import Base, BaseModel
from sqlalchemy import Table, MetaData, ForeignKey, Column, String, Text, Integer
from sqlalchemy.orm import mapper, relationship
from models.engine.db import Database


class Profile(BaseModel, Base):
    """
    Profile class
    Inherits from BaseModel and Base
    """
    __tablename__ = 'Profile'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(String(128), ForeignKey('Users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('Category.id'), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(255), nullable=True)
    payment = Column(String(128), nullable=True)
    availability = Column(String(128), nullable=True)
    linkedin = Column(String(255), nullable=True)
    github = Column(String(255), nullable=True)
    reviews = Column(Text, nullable=True)


    def __init__(self, *args, **kwargs):
        """Initializes the Profile class"""
        super(Profile, self).__init__(*args, **kwargs)


from models.user import User
from models.category import Category
# Declares table relationship after class declaration to avoid circular imports
Profile.user = relationship("User", back_populates="profile", uselist=False)
Profile.category = relationship("Category", back_populates="profile", uselist=False)