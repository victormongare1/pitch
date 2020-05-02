from . import db
from datetime import datetime
class User(db.model):
  '''
  user class to define user objects
  '''
  __tablename__='users'
class Comment(db.model):
  '''
  comment class to define comment objects
  ''' 
  __tablename__='comments'
