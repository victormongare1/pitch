from flask import render_template
from . import auth

@auth.route('/login')
def login():
  return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.index"))    

@auth.route('/register',methods=["GET","POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(email=form.email.data,username=form.username.data,password=form.password.data) 
    db.session.add(user)
    db.session.commit()
    mail_message("Welcome to watchlist","email/welcome_user",user.email,user=user)

    return redirect(url_for('auth.login'))
    title="New Account"
  return render_template('auth/register.html',registration_form=form)     