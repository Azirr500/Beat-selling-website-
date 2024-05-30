# Beat-selling-website-
My thesis for a Beat selling website 

Overview
This Beat Selling Website allows users to register, log in, view and purchase beats, and manage their profile. The website includes the following main components:

HTML Templates: Used for rendering different pages of the website.
Python Scripts: Backend logic for handling database operations, user authentication, and routing.
HTML Templates
base.html: Base template that includes common HTML structure and navigation.
index.html: Homepage template.
home.html: Home page shown to logged-in users.
profile.html: User profile page.
about.html: About page with information about the website creator.
login.html: Login page for users.
register.html: Registration page for new users.
cart.html: Shopping cart page where users can view and manage their cart items.
add_beat.html: Page for adding new beats (accessible to admins).
beats.html: Page displaying all available beats.
Python Scripts
app.py: Main application file that initializes and runs the Flask app.
add_beats.py: Script for adding beats to the database.
assign_roles.py: Script for assigning user roles.
create_admin.py: Script for creating an admin user.
extensions.py: File for initializing Flask extensions.
forms.py: Contains WTForms for handling form inputs.
init_db.py: Script for initializing the database.
models.py: Defines database models.
routes.py: Contains route handlers for different endpoints.
Step-by-Step Instructions to Run the Website

1. Clone the Repository

bash
git clone <repository-url>
cd <repository-directory>

2. Set Up Virtual Environment

bash
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the root directory and add the following variables:

makefile
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=<your-secret-key>
SQLALCHEMY_DATABASE_URI=sqlite:///site.db   # or your preferred database URI

5. Initialize the Database

csharp
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

6. Create Admin User

python create_admin.py

7. Run the Application

arduino

flask run

8. Access the Website

Open your web browser and go to http://127.0.0.1:5000/.

Detailed Explanation of Each Component
base.html

Contains the basic structure of the HTML document.
Includes navigation links to different pages.
Uses Jinja2 templating to dynamically insert content.
index.html, home.html, profile.html, about.html

Extend base.html.
Define specific content for each page within the {% block content %} section.
login.html, register.html

Extend base.html.
Include form fields using WTForms.
Display validation errors if any.
cart.html

Extends base.html.
Displays items in the user's cart.
Allows users to remove items and proceed to checkout.
add_beat.html, beats.html

Extend base.html.
add_beat.html provides a form for admins to add new beats.
beats.html displays available beats and provides options to add them to the cart.
app.py

Initializes the Flask app.
Configures database and other extensions.
Registers blueprints for different parts of the app.
add_beats.py, assign_roles.py, create_admin.py

Scripts for managing database operations and user roles.
create_admin.py is used to create an initial admin user.
extensions.py

Initializes Flask extensions like SQLAlchemy, Migrate, and LoginManager.
forms.py

Defines form classes using WTForms for handling user inputs in login, registration, and beat addition.
init_db.py

Script for initializing the database and creating necessary tables.
models.py

Defines database models such as User, Beat, and CartItem.
routes.py

Contains route handlers for rendering templates and handling form submissions.
Includes logic for user authentication, cart management, and beat handling.
