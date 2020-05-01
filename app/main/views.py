from flask import render_template
from . import main

#views
@main.route('/')
def index():
  '''view root that returns index page'''
  return render_template('index.html')  

