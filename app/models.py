from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
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
  profile_pic_path=db.Column(db.String())
  
  pitches=db.relationship('Pitch',backref='user',lazy="dynamic")
  comment=db.relationship('Comment',backref='user',lazy='dynamic')
  
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  @password.setter
  def password(self,password):
    self.pass_secure=generate_password_hash(password)
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password) 
  def save_user(self):
    db.session.add(self)
    db.session.commit()  
  def get_pitches():
    user=User.query.filter_by(id=self.id).first()
    return user.pitches   
  def __repr__(self):
    return f'User {self.username}' 

class Pitch(db.Model):
  '''
  pitch class to define pitch objects
  '''
  __tablename__ ='pitches'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(700))
  category = db.Column(db.String)
  posted = db.Column(db.DateTime, default=datetime.utcnow)
  upvotes = db.Column(db.Integer)
  downvotes = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

  def save_pitch(self):
    """
    Method that saves a pitch to the database
    """
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches(cls,category):
    pitches = Pitch.query.filter_by(category=category).all()
    return pitches  

  @classmethod
  def get_pitch(cls,id):
    pitch=Pitch.query.filter_by(id=id).first()
    return pitch

  @classmethod
  def count_pitches(cls,uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id=user.id).all()
    pitches_count = 0
      for pitch in pitches:
        pitches_count += 1
      return pitches_count
  def get_comments(self):
    """
    Method that retrieves a pitch's comments.
    """
    pitch = Pitch.query.filter_by(id = self.id).first()
    comments = Comment.query.filter_by(pitch_id = pitch.id).all()
    return comments    
class Comment(db.Model):
  '''
  comment class to define comment objects
  ''' 
  __tablename__='comments'
  id = db.Column(db.Integer,primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
  description = db.Column(db.String))
  
  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    """
    Method used for debugging the database.
    """
    return f'User {self.content}'  