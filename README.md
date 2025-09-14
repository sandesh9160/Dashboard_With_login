# 🛡️ Dashboard with JWT Login (Django REST Framework)

![Django](https://img.shields.io/badge/Django-4.2-green?logo=django) ![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python) ![DRF](https://img.shields.io/badge/DRF-RESTful-orange) ![JWT](https://img.shields.io/badge/JWT-Authentication-red)

A **simple Django REST Framework** project implementing **JWT authentication** with fully functional API endpoints for:

- User registration  
- Login (Access & Refresh tokens)  
- Protected dashboard  
- Token refresh  
- Logout & refresh token blacklist  

All APIs are tested using **JWT headers**—no Postman required.  

---

## ⚡ Features

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/register/` | POST | Register a new user |
| `/api/token/` | POST | Login & obtain JWT (access & refresh tokens) |
| `/api/dashboard/` | GET | Protected endpoint (JWT required) |
| `/api/token/refresh/` | POST | Refresh access token |
| `/api/logout/` | POST | Logout & blacklist refresh token |

---

## 📝 Requirements

- Python 3.12+  
- Django 4.2+  
- djangorestframework  
- djangorestframework-simplejwt  

Install dependencies:
pip install django djangorestframework djangorestframework-simplejwt 

# 🚀 Project Setup

# Clone the repository:

- git clone <your-repo-url>
- cd Dashboard_With_login


# Apply migrations:

python manage.py makemigrations
python manage.py migrate


# Create a superuser:

python manage.py createsuperuser


Run the development server:

python manage.py runserver

🧪 Testing JWT APIs

Since SessionAuthentication is removed, all protected endpoints require JWT headers.

# 1️⃣ Register a new user

Endpoint: http://127.0.0.1:8000/api/register/
Method: POST
Payload:

{
  "username": "sandesh",
  "email": "sandesh@example.com",
  "password": "test1234"
}


Response: User created successfully.

# 2️⃣ Obtain JWT tokens (Login)

Endpoint: http://127.0.0.1:8000/api/token/
Method: POST
Payload:

{
  "username": "sandesh",
  "password": "test1234"
}


Response:

{
  "refresh": "<REFRESH_TOKEN>",
  "access": "<ACCESS_TOKEN>"
}


Copy the access token to use in protected endpoints.

# 3️⃣ Access protected dashboard

Endpoint: http://127.0.0.1:8000/api/dashboard/
Method: GET
Headers:

Authorization: Bearer <ACCESS_TOKEN>


Response:

{
  "user": "sandesh",
  "message": "Hello sandesh"
}


You can use curl, httpie, or browser extensions like ModHeader to send headers.

# 4️⃣ Refresh access token

Endpoint: /api/token/refresh/
Method: POST
Payload:

{
  "refresh": "<REFRESH_TOKEN>"
}


Response:

{
  "access": "<NEW_ACCESS_TOKEN>"
}

# 5️⃣ Logout

Endpoint: /api/logout/
Method: POST
Payload:

{
  "refresh": "<REFRESH_TOKEN>"
}


Response:

{
  "message": "Logout successful"
}


The refresh token is now blacklisted and cannot be used again.

🌿 Git Branch Workflow

Rename local master → main:

git branch -m master main


Push to remote:

  git push -u origin main ``` bash


If the remote has existing commits:

 git pull origin main --allow-unrelated-histories
git push origin main


Use --force only if you want to overwrite remote history.

# ⚠️ Notes

Protected endpoints will always return 401 Unauthorized if JWT header is missing.

Access token expires in 5 minutes (default).

Refresh token expires in 1 day (default).

```bash
pip install django djangorestframework djangorestframework-simplejwt
