from flask import Flask
from extensions import db, bcrypt, login_manager, migrate, csrf
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)
csrf.init_app(app)

from routes import main, auth

app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
