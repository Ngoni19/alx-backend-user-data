#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """SQLAlchemy model representing a user.

    Attributes:
        id (int): The user's unique identifier.
        email (str): The user's email address.
        hashed_password (str): The user's hashed password.
        session_id (str): The user's session ID (optional).
        reset_token (str): The user's reset token (optional).
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
