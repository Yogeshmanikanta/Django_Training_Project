# Smart Campus Portal

A full-stack campus management system built to simplify and digitalize daily academic and administrative activities. The platform provides role-based access for students, faculty, and administrators, making campus operations more organized, efficient, and accessible.

## Features

### Student Module
- View attendance records
- Access study materials and resources
- View upcoming events and announcements
- Submit lost & found requests
- Book campus halls/resources

### Faculty Module
- Mark and manage student attendance
- Upload academic resources
- Manage event schedules
- Track student academic activities

### Admin Module
- Manage students, faculty, and departments
- Monitor platform activities
- Approve hall bookings
- Manage lost & found requests
- Control access permissions

## Key Functionalities
- Role-based dashboards
- Attendance management system
- Hall booking system
- Event scheduler
- Lost & found portal
- Resource repository
- Admin management panel

## Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS

### Database
- SQLite *(or update if you used another database)*

### Tools
- Git
- GitHub

## Project Structure

```bash
Smart-Campus-Portal/
│
├── campus_portal/
├── students/
├── faculty/
├── admin_panel/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Smart-Campus-Portal
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run server

```bash
python manage.py runserver
```

## Future Improvements
- Email notifications
- QR-based attendance
- AI chatbot for student support
- Placement and internship portal
- Analytics dashboard

## Learning Outcomes
Through this project, I gained practical experience in:
- Full-stack web development
- Django project architecture
- Database design and management
- Role-based authentication and authorization
- Real-world problem solving

## Author

**Yogesh Manikanta**
GitHub: `your-github-profile`
