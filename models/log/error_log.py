#!/usr/bin/python3
"""A log module - that logs messages"""
from datetime import datetime
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, DateTime


class Logger(Base, BaseModel):
    """
    A class Logger that logs messages
    """
    __tablename__ = 'error_log'
    id = Column(String(255), primary_key=True, nullable=False, autoincrement=True)
    object_affected = Column(String, nullable=False)
    level = Column(String, nullable=False)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        """
        The Logger class representation
        """
        return "id = {}, message = {}, timestamp = {}".format(
            self.id, self.message, self.timestamp)

    def save_log(self, msg=None, obj=None, level=None):
        """
        Saves the error log
        
        Args:
            msg (str): The log message.
            obj (str): The object affected by the log.
            level (str): The severity level of the log.
        """
        if level:
            try:
                self.message = msg
                self.object_affected = obj
                self.level = level
                self.save()
            except Exception as e:
                pass