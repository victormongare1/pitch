from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch

#views
@main.route('/')
def index():
  '''view root that returns index page'''
  return render_template('index.html')  

@main.route('/product')
def product():
  return render_template('product.html')

@main.route('/interview')
def interview():
  return render_template('interview.html')

@main.route('/promotion')
def promotion():
  return render_template('promotion.html')

@main.route('/motivation')
def motivation():
  return render_template('motivation.html')  
@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
  return render_template("profile/profile.html", user = user)

