from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    content = Column(Text)
    summary = Column(Text)
    link = Column(Text, unique=True)
    published = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())