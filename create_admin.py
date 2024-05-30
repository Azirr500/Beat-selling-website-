from app import app
from extensions import db, bcrypt
from models import User, Role

def create_admin():
    with app.app_context():
        admin_email = 'admin@example.com'
        admin_password = 'adminpassword'
        hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        
        # Ensure the Admin role exists
        admin_role = Role.query.filter_by(name='Admin').first()
        if not admin_role:
            admin_role = Role(name='Admin')
            db.session.add(admin_role)
            db.session.commit()

        # Create the admin user
        admin_user = User(username='admin', email=admin_email, password=hashed_password)
        admin_user.roles.append(admin_role)  # Assign the Admin role
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    create_admin()
