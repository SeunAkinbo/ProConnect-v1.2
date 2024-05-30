#!/usr/bin/python3
"""user Module"""

from models.base_model import Base, BaseModel
from resource.img_processor import ImageProcessor
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Date
from hashlib import sha256


class User(BaseModel, Base):
    """
    The User class model
    Inherits from Base and BaseModel
    """
    __tablename__ = 'Users'
    id = Column(String(128), primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    profile_picture = Column(String(128), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the User class"""
        super(User, self).__init__(*args, **kwargs)
        if kwargs:
            if "profile_picture" in kwargs.keys():
                kwargs["profile_picture"] = ImageProcessor(
                    kwargs["profile_picture"]).resize()
                super().__setattr__("profile_picture", kwargs["profile_picture"])

    def __repr__(self):
        """User class representation"""
        return "{} id='{}', created_at='{}', updated_at='{}', email='{}',first_name='{}', last_name='{}', date_of_birth='{}'".format(
            self.__class__.__name__, self.id, self.created_at, self.updated_at,
            self.email, self.firstname, self.lastname, self.date_of_birth)

    def __setattr__(self, name, value):
        """
        The class __setattr__

        Args:
            name - String
            value - String
        """
        if name == "password" and isinstance(value, str):
            value = sha256(value.encode("UTF-8")).hexdigest()
        super().__setattr__(name, value)

    def save_picture(self):
        """
        Saves the profile picture
        """
        if self.profile_picture:
            self.profile_picture = ImageProcessor(
                self.profile_picture).resize()
            self.save()

    def to_dict(self):
        """Updates the dictionary of class properties"""
        new_dict = self.__dict__.copy()
        new_dict.pop('_sa_instance_state', None)
        new_dict.pop('password', None)
        return new_dict


from models.profile import Profile
# Declares the table relationships after class declaration to avoid circular imports
User.education = relationship("Education", back_populates="user", uselist=False)
User.profile = relationship("Profile", back_populates="user", uselist=False)