#!/usr/bin/python3
"""Module - education"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Education(Base, BaseModel):
    """
    Education class
    Inherits from Base and BaseModel
    """
    __tablename__ = 'Education'
    user_id = Column(String, ForeignKey('Users.id'), nullable=False)
    education_level = Column(String(128), nullable=False)
    field_of_study = Column(String(128), nullable=False)
    name_of_institution = Column(String(128), nullable=False)
    year_of_graduation = Column(Date, nullable=False)
    country_of_study = Column(String(128), nullable=False)
    degree = Column(String(128), nullable=False)
    certification = Column(String(128), nullable=False)
    user = relationship("User", back_populates="education", uselist=False)

    def __repr__(self):
        """The class representation"""
        return "{} (id='{}', created_at = '{}',\
            updated_at = '{}', education_level='{}',\
            field_of_study='{}', name_of_institution='{}'\
            year_of_graduation='{}', country_of_study='{}'\
            degree='{}', certification='{}')".format(
            self.__class__.__name__, self.user_id, self.created_at, self.updated_at,
            self.education_level, self.field_of_study,
            self.name_of_institution, self.year_of_graduation,
            self.country_of_study, self.degree, self.certification)
