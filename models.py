from numbers import Integral
import os
from xmlrpc.client import DateTime, boolean 
from flask_sqlalchemy import SQLAlchemy
# from pytz import timezone
from sqlalchemy import Column,Integer,String,Date,Boolean
from sqlalchemy.sql import func
import json                                      
from settings import DB_NAME, DB_PASSWORD,DB_USER


database_path=os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)


db = SQLAlchemy()
def setup_database(app,path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"]=database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.app=app
    db.init_app(app)
    db.create_all()

    







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




