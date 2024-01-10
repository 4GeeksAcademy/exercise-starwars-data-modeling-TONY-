import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(250), unique=False, nullable=False)
    last_name = Column(String(250), unique=False, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), unique=False, nullable=False)
    subscription_date = Column(Integer, unique=False, nullable=True)
    favorito = relationship('Favorito')
    

    def to_dict(self):
        return {
              "id": self.id,
              "name": self.name,
              "last_name": self.last_name,
              "email": self.email,
              "subscription_date": self.subscription_date
        }

class Personaje(Base):
    __tablename__ = 'personaje'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(250), unique=False, nullable=False)
    race = Column(String(250), unique=False, nullable=False)
    favorito = relationship("favorito")

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name, 
            "race" : self.race
        }

class Planeta(Base):
    __tablename__ = 'planeta'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(250), unique=False, nullable=False)
    favorito = relationship("favorito")

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name
        }

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, unique=True, primary_key=True)
    id_usuario= Column(Integer, ForeignKey("usuario.id"))
    id_planeta= Column(Integer, ForeignKey("planeta.id"))
    id_personaje= Column(Integer, ForeignKey("personaje.id"))


    def to_dict(self):
        return {
            "id_planeta" : self.id_planeta,
            "id_personaje" : self.id_personaje
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
