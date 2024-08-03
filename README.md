# CRUD App
This is a simple CRUD (Create, Read, Update, Delete) Web-app built using Django. The app allows users register and login to perform basic operations on entries in the database.

## Features
- Responsive design for mobile and desktop
- Create new entries
- Read and display entries
- Update existing entries
- Delete entries
- User Registration/Login

<!-- ## Demo -->

<!-- You can see a live demo of the portfolio [here](http://example.com). -->

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x or higher
- Django 5.x or higher
- pip (Python package installer)
- virtualenv (optional, but recommended)



## Installation

1. **Clone the repository:**
Use SSH to clone the repository:
   ```bash 
    git clone github.com/zaidkhuroo/CRUD_Django.git
    cd CRUD_Django
   
2. **Create a virtual environment:**
   ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`


3. **Apply migrations:**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

4. **Run the development server:**
   ```bash
    python manage.py runserver

5. **Access the application:**
Open your web browser and go to http://127.0.0.1:8000/
