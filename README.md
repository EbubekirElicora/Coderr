<div align="center">

# Coderr

### Full-Stack Marketplace Application

A full-stack marketplace where customers can discover and order digital services from business users.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Visit_Coderr-1B73E8?style=for-the-badge&logo=googlechrome&logoColor=white)](https://coderr.ebubekir-elicora.de/)
[![Django](https://img.shields.io/badge/Django-6-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-API-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

</div>

---

## Table of Contents

- [Project Overview](#project-overview)
- [Live Deployment](#live-deployment)
- [Implemented Features](#implemented-features)
- [Demo Accounts](#demo-accounts)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Local Development](#local-development)
- [API Configuration](#api-configuration)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [Query Parameters](#query-parameters)
- [Permission Rules](#permission-rules)
- [Production Deployment](#production-deployment)
- [Development Checks](#development-checks)
- [Security Notes](#security-notes)
- [Additional Documentation](#additional-documentation)
- [Origin and License](#origin-and-license)
- [Author](#author)

---

## Project Overview

Coderr is a full-stack marketplace application in which two different user types interact with each other:

- Customers can browse offers, place demo orders and review business users.
- Business users can create service offers and manage orders related to their offers.

The application consists of:

- A static frontend built with HTML, CSS and JavaScript
- A Django REST Framework backend
- Token-based authentication
- Role-based permissions
- Customer and business profiles
- Offers with three service packages
- Orders and order-status management
- Ratings and reviews
- A production deployment on Google Cloud

This monorepo contains both application parts:

```text
frontend/
backend/
```

---

## Live Deployment

### Application

https://coderr.ebubekir-elicora.de/

### Public API Example

https://coderr.ebubekir-elicora.de/api/base-info/

### Repository

https://github.com/EbubekirElicora/Coderr

The deployed frontend and backend are served through the same HTTPS domain.

---

## Implemented Features

### Authentication

- Customer and business registration
- Login with DRF token authentication
- Guest demo accounts
- Automatic authentication-state handling
- Logout functionality
- Protected API requests
- Role-based permissions
- Django password hashing

### Profiles

- Customer profiles
- Business profiles
- Profile editing
- Profile-image uploads
- Location and contact information
- Business descriptions
- Working-hours information
- Profile information visible within the application
- Users can only update their own profiles

### Offers

- Display available service offers
- Search offers
- Filter offers
- Sort offers by price or update date
- Paginated offer lists
- Detailed offer pages
- Three service packages per offer
- Basic, standard and premium package types
- Offer creation by business users
- Offer editing and deletion by owners
- Delivery-time and revision information
- Individual package features and prices

### Orders

- Customers can create demo orders
- Orders are created from an offer-detail ID
- Customers can view their own orders
- Business users can view orders related to their offers
- Business users can update related order statuses
- Active-order statistics
- Completed-order statistics
- Only administrators can delete orders
- No real payment processing is included

### Reviews

- Customers can review business users
- Ratings and review descriptions
- Reviews can be edited by their owners
- Reviews can be deleted by their owners
- Business profiles display ratings
- Marketplace statistics include review counts
- Marketplace statistics include average ratings
- One review per customer and business-user combination

### Legal and Privacy Information

- Imprint
- Privacy policy
- Information about user accounts
- Information about Local Storage
- Information about server hosting
- HTTPS encryption
- No analytics or advertising cookies
- No marketing-tracking services

---

## Demo Accounts

The deployed application provides two demo accounts.

### Demo Customer

```text
Username: Demo-Kunde
Password: DemoPassword123!
```

The demo customer can:

- Browse offers
- Create orders
- View their own orders
- Create reviews
- Edit or delete their own reviews

### Demo Business User

```text
Username: Demo-Anbieter
Password: DemoPassword123!
```

The demo business user can:

- Create offers
- Edit their own offers
- Delete their own offers
- View related orders
- Update related order statuses

Both demo users are normal non-staff users.

Only staff or superuser accounts can access the Django administration area.

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- Browser Local Storage
- Responsive layouts
- Static HTML pages

### Backend

- Python 3.12+
- Django 6
- Django REST Framework
- DRF Token Authentication
- Django Filter
- Django CORS Headers
- Pillow
- SQLite

### Production Infrastructure

- Google Cloud Compute Engine
- Ubuntu Server
- Nginx
- Gunicorn
- Supervisor
- Certbot
- Let's Encrypt
- HTTPS
- DNS management

### Development Tools

- Git
- GitHub
- Visual Studio Code
- Postman
- Windows PowerShell
- Linux shell
- Django Admin

---

## Architecture

```text
Browser
   │
   ▼
Nginx
   ├── /          → Static Coderr frontend
   ├── /api/      → Gunicorn → Django REST Framework
   ├── /admin/    → Django administration
   ├── /static/   → Collected Django static files
   └── /media/    → Uploaded profile and offer images
```

The frontend communicates with the backend through REST API requests.

Protected API requests include the authentication token in the request header:

```text
Authorization: Token <token>
```

The production backend runs internally through Gunicorn on:

```text
127.0.0.1:8002
```

Port `8002` is not exposed directly to the internet.

Nginx handles public requests and forwards API and administration requests internally to Gunicorn.

Supervisor keeps the Gunicorn process running and restarts it when required.

---

## Repository Structure

```text
Coderr/
├── backend/
│   ├── auth_app/
│   │   └── api/
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── core/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── marketplace_app/
│   │   └── api/
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── offer_app/
│   │   ├── models.py
│   │   └── api/
│   │       ├── permissions.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── order_app/
│   │   ├── models.py
│   │   └── api/
│   │       ├── permissions.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── profile_app/
│   │   ├── models.py
│   │   └── api/
│   │       ├── permissions.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── review_app/
│   │   ├── models.py
│   │   └── api/
│   │       ├── permissions.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── assets/
│   ├── scripts/
│   ├── shared/
│   │   ├── scripts/
│   │   └── styles/
│   ├── styles/
│   ├── business_profile.html
│   ├── customer_profile.html
│   ├── imprint.html
│   ├── index.html
│   ├── login.html
│   ├── offer.html
│   ├── offer_list.html
│   ├── own_profile.html
│   ├── privacy_policy.html
│   ├── registration.html
│   ├── CHANGELOG.md
│   ├── LICENSE.md
│   └── README.md
│
├── .gitignore
└── README.md
```

---

## Local Development

Clone the repository:

```bash
git clone https://github.com/EbubekirElicora/Coderr.git
```

Open the repository:

```bash
cd Coderr
```

### Backend Setup

Open the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv env
```

Activate it on Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source env/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Apply the database migrations:

```bash
python manage.py migrate
```

Create an administrator account when required:

```bash
python manage.py createsuperuser
```

Start the Django development server:

```bash
python manage.py runserver
```

The local API is then available at:

```text
http://127.0.0.1:8000/api/
```

The local Django administration area is available at:

```text
http://127.0.0.1:8000/admin/
```

### Frontend Setup

Open a second terminal and switch to the frontend directory:

```bash
cd frontend
```

The frontend does not require:

- npm
- a package installation
- a compilation step
- a build command

Open `index.html` with a local development server, for example with the Visual Studio Code extension **Live Server**.

The frontend expects the local backend at:

```text
http://127.0.0.1:8000/api/
```

---

## API Configuration

The frontend API configuration is located in:

```text
frontend/shared/scripts/config.js
```

The frontend distinguishes between local development and production.

### Local Development

```text
http://127.0.0.1:8000/api/
```

### Production

```text
/api/
```

In production, Nginx forwards requests below `/api/` to the Django backend.

---

## Authentication

The backend uses Django REST Framework token authentication.

Login and registration do not require authentication.

Protected endpoints require the following header:

```text
Authorization: Token <token>
```

Example frontend request:

```javascript
fetch(`${API_BASE_URL}orders/`, {
    headers: {
        Authorization: `Token ${localStorage.getItem("auth-token")}`
    }
});
```

A successful login or registration returns a token and basic user information.

Example:

```json
{
  "token": "example-token",
  "username": "business_user",
  "email": "business@test.de",
  "user_id": 2
}
```

### Browser Storage

After a successful login, the frontend stores technically necessary authentication information in Local Storage:

```text
auth-token
auth-user
auth-user-id
```

These values are used to:

- Keep the user logged in
- Identify the authenticated user
- Authorize protected API requests

The Local Storage values are removed during logout.

No analytics, advertising or marketing cookies are used.

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| POST | `/api/registration/` | Register a user and return an authentication token |
| POST | `/api/login/` | Authenticate a user and return an authentication token |

### Profiles

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/profile/<user_id>/` | Retrieve one user profile |
| PATCH | `/api/profile/<user_id>/` | Update the authenticated user's own profile |
| GET | `/api/profiles/business/` | List business profiles |
| GET | `/api/profiles/customer/` | List customer profiles |

### Offers

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/offers/` | List offers with pagination, filters, search and ordering |
| POST | `/api/offers/` | Create an offer as a business user |
| GET | `/api/offers/<offer_id>/` | Retrieve one offer |
| PATCH | `/api/offers/<offer_id>/` | Update an offer as its owner |
| DELETE | `/api/offers/<offer_id>/` | Delete an offer as its owner |
| GET | `/api/offerdetails/<offerdetail_id>/` | Retrieve one offer detail |

### Orders

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/orders/` | List orders related to the authenticated user |
| POST | `/api/orders/` | Create an order as a customer |
| GET | `/api/orders/<order_id>/` | Retrieve one order |
| PATCH | `/api/orders/<order_id>/` | Update an order status as the related business user |
| DELETE | `/api/orders/<order_id>/` | Delete an order as an administrator |
| GET | `/api/order-count/<business_user_id>/` | Return the active-order count |
| GET | `/api/completed-order-count/<business_user_id>/` | Return the completed-order count |

### Reviews

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/reviews/` | List reviews with filters and ordering |
| POST | `/api/reviews/` | Create a review as a customer |
| PATCH | `/api/reviews/<review_id>/` | Update a review as its owner |
| DELETE | `/api/reviews/<review_id>/` | Delete a review as its owner |

### Marketplace Statistics

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/base-info/` | Return general marketplace statistics |

Example response:

```json
{
  "review_count": 2,
  "average_rating": 4.0,
  "business_profile_count": 1,
  "offer_count": 5
}
```

---

## Query Parameters

### Offers

The offer-list endpoint supports:

```text
creator_id
min_price
max_delivery_time
search
ordering
page_size
```

Examples:

```text
/api/offers/?creator_id=2
/api/offers/?min_price=100
/api/offers/?max_delivery_time=5
/api/offers/?search=design
/api/offers/?ordering=min_price
/api/offers/?ordering=-min_price
/api/offers/?ordering=updated_at
/api/offers/?ordering=-updated_at
/api/offers/?page_size=6
```

Allowed ordering values:

```text
min_price
-min_price
updated_at
-updated_at
```

### Reviews

The review-list endpoint supports:

```text
business_user_id
reviewer_id
ordering
```

Examples:

```text
/api/reviews/?business_user_id=2
/api/reviews/?reviewer_id=3
/api/reviews/?ordering=rating
/api/reviews/?ordering=-rating
/api/reviews/?ordering=updated_at
/api/reviews/?ordering=-updated_at
```

Allowed ordering values:

```text
rating
-rating
updated_at
-updated_at
```

---

## Permission Rules

### General

- Login and registration are publicly accessible.
- The offer list and marketplace statistics are publicly accessible.
- Protected endpoints require token authentication.
- Staff and superuser accounts can access Django Admin.

### Profiles

- Authenticated users can retrieve profile information.
- Users can only update their own profile.

### Offers

- Business users can create offers.
- Customer users cannot create offers.
- Each offer must contain exactly three offer details.
- Offer-detail package types must be unique within an offer.
- Only the offer owner can update or delete an offer.
- Authenticated users can retrieve individual offer details.

### Orders

- Customer users can create orders.
- Business users cannot create orders.
- Orders are created using an `offer_detail_id`.
- Customers can view their own orders.
- Business users can view orders related to their offers.
- Only the related business user can update an order status.
- Only staff or administrator users can delete orders.

### Reviews

- Customer users can create reviews.
- Business users cannot create reviews.
- A customer can only review a business user once.
- Only the review creator can update or delete the review.

---

## Production Deployment

The production application uses:

- Google Cloud Compute Engine
- Ubuntu Server
- Nginx
- Gunicorn
- Supervisor
- Django REST Framework
- SQLite
- Certbot
- Let's Encrypt
- HTTPS

The public application is available at:

```text
https://coderr.ebubekir-elicora.de/
```

The public API is available below:

```text
https://coderr.ebubekir-elicora.de/api/
```

The Django administration area is available below:

```text
https://coderr.ebubekir-elicora.de/admin/
```

The backend application is bound internally to:

```text
127.0.0.1:8002
```

Public requests are handled by Nginx.

### Production Environment Variables

Production settings use environment variables such as:

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
```

Example structure:

```text
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,coderr.ebubekir-elicora.de
```

Real production secrets must never be committed to GitHub.

---

## Development Checks

Run the following commands from the `backend` directory.

Check the Django configuration:

```bash
python manage.py check
```

Check whether model changes require migrations:

```bash
python manage.py makemigrations --check --dry-run
```

Create migrations when required:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Check installed Python dependencies:

```bash
python -m pip check
```

Update `requirements.txt` on Windows:

```powershell
cmd /c "python -m pip freeze > requirements.txt"
```

Update `requirements.txt` on Linux or macOS:

```bash
python -m pip freeze > requirements.txt
```

### Frontend Checks

Before committing frontend changes:

- Test registration
- Test login and logout
- Test customer accounts
- Test business accounts
- Test offer creation
- Test offer filters and search
- Test order creation
- Test order-status updates
- Test review creation
- Test profile editing
- Check the browser console
- Test the imprint
- Test the privacy policy
- Test the application responsively

---

## Security Notes

The repository excludes sensitive or generated files through `.gitignore`.

Do not commit:

```text
db.sqlite3
*.sqlite3
.env
.env.*
env/
venv/
.venv/
media/
staticfiles/
__pycache__/
*.log
```

Additional security measures include:

- Django password hashing
- Token authentication
- Server-side permission checks
- Role-based endpoint restrictions
- HTTPS/TLS encryption
- Production secrets stored outside Git
- Nginx as reverse proxy
- Gunicorn bound to an internal port
- Restricted Django administration access

---

## Additional Documentation

Detailed documentation for each part of the application remains available inside the monorepo.

### Backend Documentation

[`backend/README.md`](./backend/README.md)

Includes:

- Complete backend setup
- Authentication documentation
- Endpoint documentation
- Query parameters
- Response formats
- Permission rules
- Production environment variables
- Deployment commands
- Development checks

### Frontend Documentation

[`frontend/README.md`](./frontend/README.md)

Includes:

- Frontend features
- Local setup
- API configuration
- Authentication storage
- Backend communication
- Deployment information
- Development notes

---

## Origin and License

The Coderr frontend is based on the project template provided by the Developer Akademie.

It was extended, connected to a separately implemented Django REST Framework backend and deployed as a full-stack portfolio project.

The original frontend license information is retained in:

```text
frontend/LICENSE.md
```