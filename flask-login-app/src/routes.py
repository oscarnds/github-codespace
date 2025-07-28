from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .forms import LoginForm

routes = Blueprint('routes', __name__)

# Simulated user data for validation
users = {
    "admin": "password123",
    "user": "mypassword"
}

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and users[username] == password:
            session['username'] = username
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('routes.home'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
    return render_template('login.html', form=form)

@routes.route('/home')
def home():
    if 'username' not in session:
        flash('Por favor inicie sesión primero', 'warning')
        return redirect(url_for('routes.login'))
    return render_template('home.html', username=session['username'])

@routes.route('/logout')
def logout():
    session.pop('username', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('routes.login'))