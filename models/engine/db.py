#!/usr/bin/python3
"""
Database Storage Module
"""

import models
import os
from models.log.error_log import Logger
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

objects = {"User": "User", "Education": "Education", "Payment": "Payment"}


class Database:
    """
    Database class - Interacts with MySQL database
    """
    __session = None
    __engine = None

    def __init__(self):
        """
        Instantiates the Database class
        """
        DATABASE_CONGIG = {
            'LOCALHOST': 'localhost',
            'USERNAME': 'root',
            'PASSWORD': 'ProConnectAdmin',
            'PROCONNECT_DB': 'ProConnectDB'
        }
        
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(DATABASE_CONGIG['USERNAME'],
                                               DATABASE_CONGIG['PASSWORD'],
                                               DATABASE_CONGIG['LOCALHOST'],
                                               DATABASE_CONGIG['PROCONNECT_DB']))

            Base.metadata.create_all(self.__engine)
        except Exception as e:
            Logger().save_log(str(e), __class__.__name__, "Database_Error")

    def reload(self):
        """Reloads the database"""
        if self.__engine is None:
            raise ValueError("Database is not initialized")
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(SessionFactory)
    
    def new(self, obj):
        """
        Add an object to the current database session

        Args:
            obj - Current class object
        """
        if self.__session:
            try:
                self.__session.add(obj)
            except Exception as e:
                Logger().save_log(str(e), __class__.__name__, "Database_Error")

    def save(self):
        """Commit all current database session changes"""
        if self.__session:
            try:
                self.__session.commit()
            except Exception as e:
                Logger().save_log(str(e), __class__.__name__, "Database_Error")

    def all(self, cls=None):
        """
        Queries the current database for all object instances

        Args:
            cls - class object to be queried
        """
        obj_instance = {}
        for obj in objects:
            if cls is None or cls is objects[obj] or cls is obj:
                try:
                    objs = self.__session.query(objects[obj]).all()
                    for _ in objs:
                        key = "{}_{}".format(_.__class__.__name__, _.id)
                        obj_instance[key] = _
                except Exception as e:
                    Logger().save_log(str(e), __class__.__name__, "Database_Error")
        return obj_instance

    def delete(self, obj=None):
        """
        Delete an object from the current database session

        Args:
            obj - Current class object
        """
        if obj is not None and self.__session:
            self.__session.delete(obj)

    def close(self):
        """Close the current database session"""
        if self.__session:
            try:
                self.__session.close()
            except Exception as e:
                Logger().save_log(str(e), __class__.__name__, "Database_Error")

    def get_object(self, obj, id):
        """
        Retrieves an object from the current database

        Args:
            cls - The class to inspect
            id - The id of the object
        """
        if obj not in objects.values():
            return None
        try:
            all_object_instances = models.database.all(obj)
            for item in all_object_instances.values():
                if item.id == id:
                    return item
        except Exception as e:
            Logger().save_log(str(e), __class__.__name__, "Database_Error")
        return None

    def count_objects(self, obj=None):
        """
        Counts the number of objects in the database

        Args:
            obj - The class to retrive and count
        """
        if obj:
            if isinstance(models.database.all(obj), dict):
                return len(models.database.all(obj).values())
            return len(models.database.all(obj))
        objs = objects.values()
        total_object = 0
        for item in objs:
            total_object += len(models.database.all(item).values())
        return total_object    
