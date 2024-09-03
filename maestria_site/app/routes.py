from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db  # Importe `db` corretamente
from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sobre.html')
def sobre_nos():
    return render_template('sobre.html')

@main.route('/servicos.html')
def servicos():
    return render_template('servicos.html')

@main.route('/projetos.html')
def projetos():
    return render_template('projetos.html')

@main.route('/depoimentos.html')
def depoimentos():
    return render_template('depoimentos.html')

@main.route('/contato.html', methods=['GET', 'POST'])
def contato():
    form = ContactForm()
    if form.validate_on_submit():
        # Lógica para enviar e-mail
        flash('Your message has been sent.')
        return redirect(url_for('home'))
    return render_template('contato.html', form=form)

@main.route('/login.html', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('home'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)

@main.route('/cadastro.html', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful.')
        return redirect(url_for('login'))
    return render_template('cadastro.html', form=form)

@main.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('home'))

@main.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Access denied.')
        return redirect(url_for('home'))
    return render_template('admin.html')
