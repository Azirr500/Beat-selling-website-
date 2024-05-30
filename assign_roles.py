from app import app
from extensions import db
from models import Role

def create_roles():
    with app.app_context():
        admin_role = Role(name='Admin')
        user_role = Role(name='User')
        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.commit()

if __name__ == '__main__':
    create_roles()
