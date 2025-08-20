Employee Management API

A Django REST Framework (DRF) powered API for managing employees, departments, attendance, and performance.
This project demonstrates API design, authentication with JWT, and containerization using Docker.

🚀 Features

Employee CRUD (Create, Read, Update, Delete)

Department management

Attendance tracking

Performance reviews

JWT-based authentication

Role-based permissions

API documentation with Swagger

Docker & docker-compose support

🛠️ Tech Stack

Backend: Django 5, Django REST Framework (DRF)

Authentication: JWT (SimpleJWT)

Database: PostgreSQL (default: SQLite for local dev)

Docs: Swagger (drf-yasg)

Containerization: Docker, docker-compose

📂 Project Structure
employee_project/
│── employees/            # Employee & Department apps
│── attendance/           # Attendance app
│── performance/          # Performance app
│── employee_project/     # Project settings & URLs
│── requirements.txt      # Dependencies
│── Dockerfile            # Docker build file
│── docker-compose.yml    # Multi-container setup
│── .env.example          # Example environment file
│── README.md             # Project documentation


⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/13PARAG/employee-management-api.git
cd employee-management-api

2️⃣ Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment

Copy .env.example to .env and fill in values (DB, secret key, etc.).
Example:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/employee_db

5️⃣ Run migrations
python manage.py migrate

6️⃣ Create superuser
python manage.py createsuperuser

7️⃣ Run server
python manage.py runserver


Access at:

Swagger Docs → http://127.0.0.1:8000/swagger/

Admin Panel → http://127.0.0.1:8000/admin/

🐳 Running with Docker
docker-compose up --build

🔑 Authentication

JWT authentication via /api/token/ and /api/token/refresh/

Include token in headers:

Authorization: Bearer <your_token>

📌 Quick API Reference
🔹 Authentication

POST /api/token/ → Get JWT token

POST /api/token/refresh/ → Refresh token

🔹 Employees

GET /employees/ → List employees

POST /employees/ → Create employee

GET /employees/{id}/ → Retrieve employee

PUT /employees/{id}/ → Update employee

DELETE /employees/{id}/ → Delete employee

🔹 Departments

GET /departments/ → List departments

POST /departments/ → Create department

🔹 Attendance

GET /attendance/ → List attendance records

POST /attendance/ → Mark attendance

🔹 Performance

GET /performance/ → List performance reviews

POST /performance/ → Add performance review

✅ Tests

Run unit tests with:

python manage.py test

📧 Author

PARAG KHANDARE

https://github.com/13PARAG
