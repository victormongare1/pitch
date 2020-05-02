from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user

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
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
  form = UpdateProfile()
  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  return redirect(url_for('main.profile',uname=uname))  