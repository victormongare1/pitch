from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
  
class User(db.Model):
  '''
  user class to define user objects
  '''
  __tablename__='users'
  id=db.Column(db.Integer,primary_key = True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255),unique=True,index=True)
  pass_secure=db.Column(db.String(255))
  password_hash=db.Column(db.String(255))
  bio=db.Column(db.String(255))
  pitches=db.relationship('Pitch',backref='user',lazy="dynamic")
  comment=db.relationship('Comment',backref='user',lazy='dynamic')


class Pitch(db.Model):
  '''
  pitch class to define pitch objects
  '''
  __tablename__ ='pitches'
   id = db.Column(db.Integer, primary_key = True)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
class Comment(db.Model):
  '''
  comment class to define comment objects
  ''' 
  __tablename__='comments'
  id = db.Column(db.Integer,primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
  description = db.Column(db.String))
