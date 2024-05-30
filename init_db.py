from app import app
from extensions import db
from create_admin import create_admin
from assign_roles import create_roles

def init_db():
    with app.app_context():
        db.create_all()
        create_roles()
        create_admin()

if __name__ == '__main__':
    init_db()
