#!/usr/bin/python3
"""
The base model module - Contains the BaseModel class
"""

import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

time_format = '%Y-%m-%dT%H:%M:%S.%f'
Base = declarative_base()

class BaseModel:
    """BaseModel class - The core of future model classes declaration"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """String representation of the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Save the current model instance to the database"""
        self.updated_at = datetime.utcnow()
        models.database.new(self)
        models.database.save()
    
    def delete(self):
        """Delete the current model instance from the database"""
        if self is not None and self:
            models.database.delete(self)

    def to_dict(self):
        """A dictionary containing all instance keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time_format)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time_format)
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict