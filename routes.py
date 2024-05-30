from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from extensions import db, bcrypt
from models import User, Beat, Cart
from forms import RegistrationForm, LoginForm, AddBeatForm

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/cart")
@login_required
def cart():
    user_cart = Cart.query.filter_by(user_id=current_user.id).all()
    total_price = sum(item.beat.price for item in user_cart)
    form = AddBeatForm()
    return render_template('cart.html', cart_items=user_cart, total_price=total_price, form=form)

@main.route("/beats")
def beats():
    all_beats = Beat.query.all()
    form = AddBeatForm()
    return render_template('beats.html', beats=all_beats, form=form)

@main.route("/add_to_cart/<int:beat_id>", methods=['POST'])
@login_required
def add_to_cart(beat_id):
    beat = Beat.query.get_or_404(beat_id)
    cart_item = Cart(user_id=current_user.id, beat_id=beat.id)
    db.session.add(cart_item)
    db.session.commit()
    flash(f'Added {beat.title} to your cart!', 'success')
    return redirect(url_for('main.beats'))

@main.route("/remove_from_cart/<int:cart_id>", methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != current_user.id:
        abort(403)
    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart', 'success')
    return redirect(url_for('main.cart'))

@main.route("/checkout", methods=['POST'])
@login_required
def checkout():
    # Implement the checkout process here (e.g., integrate with a payment gateway)
    # For now, we'll just clear the cart and show a success message
    user_cart = Cart.query.filter_by(user_id=current_user.id).all()
    for item in user_cart:
        db.session.delete(item)
    db.session.commit()
    flash('Thank you for your purchase!', 'success')
    return redirect(url_for('main.home'))

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_user:
            if existing_user.username == form.username.data:
                flash('Username already exists. Please choose a different one.', 'danger')
            elif existing_user.email == form.email.data:
                flash('Email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
        
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@auth.route("/add_beat", methods=['GET', 'POST'])
@login_required
def add_beat():
    if current_user.username != 'adminrights' or current_user.email != 'admin@beats.com':
        abort(403)  # Only allow the specific admin user to access this route
    form = AddBeatForm()
    if form.validate_on_submit():
        beat = Beat(title=form.title.data, filename=form.filename.data, price=form.price.data)
        db.session.add(beat)
        db.session.commit()
        flash('The beat has been added!', 'success')
        return redirect(url_for('main.beats'))
    return render_template('add_beat.html', form=form)

@main.route("/remove_beat/<int:beat_id>", methods=['POST'])
@login_required
def remove_beat(beat_id):
    if current_user.username != 'adminrights' or current_user.email != 'admin@beats.com':
        abort(403)  # Only allow the specific admin user to access this route
    beat = Beat.query.get_or_404(beat_id)
    db.session.delete(beat)
    db.session.commit()
    flash('The beat has been removed!', 'success')
    return redirect(url_for('main.beats'))
