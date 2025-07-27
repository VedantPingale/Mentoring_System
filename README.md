# Mentoring System

A web-based Mentoring System built using **Python (Django Framework)** and **HTML**.  
This system facilitates seamless interaction between students and mentors by allowing students to manage their academic and certification records, while enabling mentors to access this information.

## Features

- **Student Functionality:**
  - Upload personal details and certifications
  - View uploaded data
  - Delete details or certifications if needed

- **Mentor Functionality:**
  - View student profiles and submitted certifications

## Tech Stack

- **Backend:** Python (Django Framework)
- **Frontend:** HTML
- **Database:** Default Django ORM (SQLite by default)

## Setup Instructions

### Prerequisites

Before setting up the project, make sure you have the following installed on your system:

- **Python** (version 3.6 or above)  
  [Download Python](https://www.python.org/downloads/)
  or through the official microsoft store

- **pip** (Python package installer)  
  Usually comes bundled with Python. To check if it's installed:
  ```bash
  pip --version
  pip install django
  pip install django_widget_tweaks
  pip install pillow

  
### Quick Start

1. Click on **Code** (green button) and select **Download ZIP**
2. Extract the downloaded ZIP file to your desired location
3. Open the extracted folder (the one containing `manage.py`)
4. Right-click inside the folder and select **Open Terminal** or **Open Command Prompt**
5. Run the following command:
   ```bash
   python manage.py runserver
6. Open your browser and go to http://127.0.0.1:8000/ to access the website

## The Default Login for Admin is 
### Username
    Admin
### Password
    Admin@123
### Make Sure to change the admin password using the admin panel
### To add a new admin open the command prompt and enter
  ```bash
  python manage.py createsuperuser
