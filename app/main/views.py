from flask import render_template
from . import main

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


