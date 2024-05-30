"""
Initialize the models package
"""

from models.engine.db import Database
from models.base_model import BaseModel
from models.user import User
from models.education import Education

database = Database()

try:
    database.reload()
except Exception as e:
    print(f"Error: {e}")
