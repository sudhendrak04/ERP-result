# ERP Result Generation System

A full-stack web application for managing and generating student results in an educational institution.

## Features

- Student data management
- Attendance tracking
- Assignment and practical marks recording
- Internal assessment (IA) and End Semester Examination (ESE) marks management
- PDF report generation
- User authentication

## Tech Stack

### Backend
- Django 4.2.10
- Django REST Framework
- SQLite Database
- CORS Headers

### Frontend
- React.js
- HTML2PDF.js for report generation
- Modern UI with responsive design

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd django_backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd result
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Usage

1. Access the application at http://localhost:3000
2. Log in with your superuser credentials
3. Add student data
4. Generate and download PDF reports

## API Endpoints

- GET /api/students/ - List all students
- POST /api/students/ - Create a new student
- GET /api/students/{roll_no}/ - Get a specific student
- PUT /api/students/{roll_no}/ - Update a student
- DELETE /api/students/{roll_no}/ - Delete a student

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request