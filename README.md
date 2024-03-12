# School Registration System

Welcome to the School Registration System, a Django web application for managing class streams and student information.

## Features

- Create and manage class streams.
- Capture and edit student information.
- View individual students and all students in the system.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 
- Django 

### Installation

1. Clone the repository:

```bash
git clone https://github.com/rkipchumba/fintech-student-registration.git
cd school-registration-system
```

### Install the required dependencies
```bash
pip install -r requirements.txt
```

### Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Start the development server:
```bash
python manage.py runserver
```
1. Open your browser and navigate to `http://127.0.0.1:8000/student-management/class-streams/` to access the School Registration System.
2. Create class streams, capture student data, and explore the features of the system.
