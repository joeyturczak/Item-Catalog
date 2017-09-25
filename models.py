#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(80))


class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class CatalogItem(Base):

    __tablename__ = 'catalog_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    created_date = Column(DateTime(timezone=True), default=func.now())
    category_name = Column(String(80), ForeignKey('category.name'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_name': self.category_name
        }


engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
