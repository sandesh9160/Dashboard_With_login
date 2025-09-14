# Dashboard with JWT Login (Django REST Framework)

A simple Django REST Framework project with JWT authentication and API endpoints for:

User registration

Login (access & refresh tokens)

Protected dashboard

Token refresh

Logout & refresh token blacklist

All APIs are tested using JWT headers. No Postman is required, but headers must be sent to access protected endpoints.

Features

/api/register/ → User registration

/api/token/ → Login (returns access & refresh token)

/api/dashboard/ → Protected endpoint (JWT required)

/api/token/refresh/ → Refresh access token

/api/logout/ → Logout (blacklist refresh token)

Requirements

Python 3.12+

Django 4.2+

djangorestframework

djangorestframework-simplejwt

Install dependencies:

pip install django djangorestframework djangorestframework-simplejwt

Project Setup

Clone the repository:

git clone <your-repo-url>
cd Dashboard_With_login

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Testing JWT APIs in Browser

Since SessionAuthentication is removed, protected endpoints require JWT headers.

# 1️⃣ Register a new user

Open: http://127.0.0.1:8000/api/register/

Method: POST → fill JSON:

{
"username": "sandesh",
"email": "sandesh@example.com",
"password": "test1234"
}

Click POST → Execute to create a user.

# 2️⃣ Obtain JWT tokens (Login)

Open: http://127.0.0.1:8000/api/token/

Method: POST → JSON:

{
"username": "sandesh",
"password": "test1234"
}

Response:

{
"refresh": "<REFRESH_TOKEN>",
"access": "<ACCESS_TOKEN>"
}

Copy the access token for protected endpoints.

# 3️⃣ Access protected dashboard

Open: http://127.0.0.1:8000/api/dashboard/

You must include headers:

Authorization: Bearer <ACCESS_TOKEN>

Response:

{
"user": "sandesh",
"message": "Hello sandesh"
}

You can use curl, httpie, or a browser extension like ModHeader to send headers.

# 4️⃣ Refresh access token

Open: /api/token/refresh/

POST JSON:

{
"refresh": "<REFRESH_TOKEN>"
}

Response:

{
"access": "<NEW_ACCESS_TOKEN>"
}

5️⃣ Logout

Open: /api/logout/

POST JSON:

{
"refresh": "<REFRESH_TOKEN>"
}

Response:

{
"message": "Logout successful"
}

Refresh token is now blacklisted and cannot be used again.

Git Branch Workflow

Rename local master → main:

git branch -m master main

Push to remote:

git push -u origin main

If remote has existing commits:

git pull origin main --allow-unrelated-histories
git push origin main

Use --force only if you want to overwrite remote history.

**Notes**

Protected endpoints will always return 401 if JWT header is missing.

Access token expires in 5 minutes (default).

Refresh token expires in 1 day (default).

This README is ready to save as README.md in your repo.
