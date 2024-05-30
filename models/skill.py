#!/usr/bin/python3
"""skill Module"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Skill(Base, BaseModel):
    """
    The Skill class model
    Inherits from Base and BaseModel
    """
    __tablename__ = 'Skills'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    duration = Column(String(128), nullable=False)
    skill_name = Column(String(128), nullable=False)