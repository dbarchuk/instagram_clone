from app.database import Base
from sqlalchemy import Column, String, Integer


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
