from numbers import Integral
import os
from turtle import title
from xmlrpc.client import DateTime, boolean 
from flask_sqlalchemy import SQLAlchemy
# from pytz import timezone
from sqlalchemy import Column,Integer,String,Date,Boolean
from sqlalchemy.sql import func
import json                                      
from settings import DB_NAME, DB_PASSWORD,DB_USER


database_path="postgresql://{}:{}@{}/{}".format(DB_USER,DB_PASSWORD,'localhost:5432',DB_NAME)

db = SQLAlchemy()
def setup_database(app,path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"]=database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.app=app
    db.init_app(app)
    # movie=Movies(title='12 Angry Men')
    # actor=Actors(name='Henry Fonda',age='45',gender='M')
    db.create_all()
    # insert(movie)
    # insert(actor)

    







class Movies(db.Model):
    __tablename__='movies'
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    release_date=Column(String)

    # boilerplate function to serialize the object 
    def format(self):
        return{
        'id':self.id,
        'title':self.title,
        'release_date':self.release_date
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()



    def delete(self):
        db.session.delete(self)
        db.session.commit()



    def update(self):
         db.session.commit()


        



class Actors(db.Model):
    __tablename__='actors'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    age=Column(Integer)
    gender=Column(String)


    def format(self):
        return{
            'id':self.id,
            'name':self.name,
            'age':self.age,
            'gender':self.gender
        }



    def insert(self):
        db.session.add(self)
        db.session.commit()



    def delete(self):
        db.session.delete(self)
        db.session.commit()



    def update(self):
        db.session.commit()




