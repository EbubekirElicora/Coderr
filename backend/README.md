# Coderr Backend API

This directory contains the Django REST Framework backend of the Coderr full-stack marketplace application.

The complete project is maintained as a monorepo containing both the backend and frontend.

All documented API endpoints are available below:

```text
/api/
```

---

## Live Deployment

### Application

https://coderr.ebubekir-elicora.de/

### Public API Example

https://coderr.ebubekir-elicora.de/api/base-info/

### Django Administration

https://coderr.ebubekir-elicora.de/admin/

### Repository

https://github.com/EbubekirElicora/Coderr

### Frontend Source

[`../frontend/`](../frontend/)

---

## Project Overview

Coderr is a full-stack marketplace application where customers can discover and order digital services from business users.

The backend provides:

- User registration and login
- Token-based authentication
- Customer and business profiles
- Offer and package management
- Order management
- Review management
- Marketplace statistics
- Role-based permissions
- Image uploads
- Search, filtering and ordering
- Pagination
- Django administration
- Production deployment through Gunicorn and Nginx

---

## Tech Stack

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

### Development Tools

- Git
- GitHub
- Visual Studio Code
- Postman
- Windows PowerShell
- Linux shell
- Django Admin

---

## Backend Structure

```text
backend/
├── auth_app/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── marketplace_app/
│   ├── api/
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── offer_app/
│   ├── api/
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── order_app/
│   ├── api/
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── profile_app/
│   ├── api/
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── review_app/
│   ├── api/
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   └── models.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Local Setup

Clone the complete monorepo:

```bash
git clone https://github.com/EbubekirElicora/Coderr.git
```

Open the backend directory:

```bash
cd Coderr/backend
```

### Create a Virtual Environment

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

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Create an Administrator Account

```bash
python manage.py createsuperuser
```

### Start the Development Server

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

---

## Demo Accounts

The deployed application provides demo access for both supported user types.

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

Only staff or superuser accounts can access Django Admin.

---

## Authentication

The backend uses Django REST Framework token authentication.

Login and registration do not require authentication.

Protected endpoints require the following header:

```text
Authorization: Token <token>
```

A successful login or registration returns an authentication token and basic user information.

Example:

```json
{
  "token": "example-token",
  "username": "business_user",
  "email": "business@test.de",
  "user_id": 2
}
```

The frontend stores the token in the browser and includes it in protected API requests.

---

## User Types

The application supports two profile types:

```text
customer
business
```

### Customer Users

Customer users can:

- Browse offers
- View offer details
- Create orders
- View their own orders
- Create reviews
- Edit their own reviews
- Delete their own reviews
- Edit their own profile

### Business Users

Business users can:

- Create offers
- Edit their own offers
- Delete their own offers
- View orders related to their offers
- Update related order statuses
- Edit their own profile

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| POST | `/api/registration/` | Register a new user and return a token |
| POST | `/api/login/` | Authenticate a user and return a token |

---

### Profiles

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/profile/<user_id>/` | Retrieve one user profile |
| PATCH | `/api/profile/<user_id>/` | Update the authenticated user's own profile |
| GET | `/api/profiles/business/` | List business profiles |
| GET | `/api/profiles/customer/` | List customer profiles |

---

### Offers

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/offers/` | List offers with pagination, search, filters and ordering |
| POST | `/api/offers/` | Create an offer as a business user |
| GET | `/api/offers/<offer_id>/` | Retrieve one offer |
| PATCH | `/api/offers/<offer_id>/` | Update an offer as its owner |
| DELETE | `/api/offers/<offer_id>/` | Delete an offer as its owner |
| GET | `/api/offerdetails/<offerdetail_id>/` | Retrieve one offer detail |

Each offer contains three service packages:

```text
basic
standard
premium
```

Each package can contain:

- Title
- Description
- Price
- Delivery time
- Number of revisions
- Individual features

---

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

Orders are created using an offer-detail ID:

```json
{
  "offer_detail_id": 1
}
```

---

### Reviews

| Method | Endpoint | Description |
| :---: | :--- | :--- |
| GET | `/api/reviews/` | List reviews with filters and ordering |
| POST | `/api/reviews/` | Create a review as a customer |
| PATCH | `/api/reviews/<review_id>/` | Update a review as its owner |
| DELETE | `/api/reviews/<review_id>/` | Delete a review as its owner |

A customer can only create one review for the same business user.

---

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

The exact values depend on the current production database.

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

---

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

## Response Formats

### Paginated Offer Response

`GET /api/offers/` returns a paginated response:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": []
}
```

### Order Response

`GET /api/orders/` returns a direct list:

```json
[]
```

### Review Response

`GET /api/reviews/` returns a direct list:

```json
[]
```

### Base-Info Response

```json
{
  "review_count": 2,
  "average_rating": 4.0,
  "business_profile_count": 1,
  "offer_count": 5
}
```

---

## Permission Rules

### General

- Login and registration are publicly accessible.
- The offer list is publicly accessible.
- Marketplace statistics are publicly accessible.
- Protected endpoints require token authentication.
- Staff and superusers can access Django Admin.

### Profiles

- Authenticated users can retrieve profile information.
- Users can only update their own profiles.

### Offers

- Business users can create offers.
- Customer users cannot create offers.
- Each offer must contain exactly three offer details.
- Offer-detail types must be unique within an offer.
- Only the offer owner can update an offer.
- Only the offer owner can delete an offer.
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
- A customer can only review the same business user once.
- Only the review creator can update a review.
- Only the review creator can delete a review.

---

## Django Admin

The local administration area is available at:

```text
http://127.0.0.1:8000/admin/
```

The production administration area is available at:

```text
https://coderr.ebubekir-elicora.de/admin/
```

Only staff or superuser accounts can access Django Admin.

---

## Production Architecture

```text
Browser
   │
   ▼
Nginx
   ├── /          → Static Coderr frontend
   ├── /api/      → Gunicorn → Django REST Framework
   ├── /admin/    → Django administration
   ├── /static/   → Collected Django static files
   └── /media/    → Uploaded media files
```

The backend runs internally through Gunicorn on:

```text
127.0.0.1:8002
```

Port `8002` is not exposed directly to the internet.

Nginx handles all public requests over HTTPS.

Supervisor keeps the Gunicorn process running and restarts it when required.

---

## Production Paths

The complete monorepo is deployed at:

```text
/var/www/projects/coderr
```

Backend:

```text
/var/www/projects/coderr/backend
```

Frontend:

```text
/var/www/projects/coderr/frontend
```

Gunicorn logs:

```text
/var/www/projects/coderr/logs
```

---

## Production Environment Variables

Production settings are passed through the Supervisor configuration.

The following environment variables are used:

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
```

Example:

```text
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,coderr.ebubekir-elicora.de
```

The real production secret key must never be committed to GitHub.

---

## Updating the Production Deployment

Connect to the server and open the monorepo directory:

```bash
cd /var/www/projects/coderr
```

Create a database backup before important backend changes:

```bash
cp backend/db.sqlite3 \
"backend/db.sqlite3.backup-$(date +%Y%m%d-%H%M%S)"
```

Pull the latest monorepo version:

```bash
git pull
```

Open the backend directory:

```bash
cd backend
```

Activate the production virtual environment:

```bash
source venv/bin/activate
```

Install new or changed dependencies:

```bash
python -m pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Collect static files:

```bash
python manage.py collectstatic --noinput
```

Check the Django configuration:

```bash
python manage.py check
```

Restart the production service:

```bash
sudo supervisorctl restart coderr
```

Check the service status:

```bash
sudo supervisorctl status coderr
```

Test the internal API:

```bash
curl http://127.0.0.1:8002/api/base-info/
```

Test the public API:

```bash
curl https://coderr.ebubekir-elicora.de/api/base-info/
```

---

## Development Checks

Run these commands from the `backend` directory.

### Django System Check

```bash
python manage.py check
```

### Check for Missing Migrations

```bash
python manage.py makemigrations --check --dry-run
```

### Create Migrations

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Check Dependencies

```bash
python -m pip check
```

### Update Requirements on Windows

```powershell
cmd /c "python -m pip freeze > requirements.txt"
```

### Update Requirements on Linux or macOS

```bash
python -m pip freeze > requirements.txt
```

---

## Security Notes

Sensitive and generated files must not be committed.

The repository excludes files such as:

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
- Role-based restrictions
- HTTPS encryption
- Production secrets outside Git
- Internal Gunicorn port
- Nginx reverse proxy
- Restricted Django Admin access

---

## Testing Checklist

Before pushing backend changes:

- Run `python manage.py check`
- Check for missing migrations
- Test registration
- Test login
- Test customer permissions
- Test business permissions
- Test profiles
- Test offer creation
- Test offer editing
- Test offer deletion
- Test offer filters
- Test offer search
- Test order creation
- Test order status updates
- Test reviews
- Test API error responses
- Test the public API after deployment
- Do not commit credentials or private data

---

## Related Documentation

### Main Project Documentation

[`../README.md`](../README.md)

### Frontend Documentation

[`../frontend/README.md`](../frontend/README.md)