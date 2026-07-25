# Coderr Backend API

This repository contains the Django REST Framework backend for the Coderr marketplace frontend.

All documented API endpoints are available below `/api/`.

## Live Deployment

Frontend:

https://coderr.ebubekir-elicora.de

Public API example:

https://coderr.ebubekir-elicora.de/api/base-info/

Frontend repository:

https://github.com/EbubekirElicora/Coderr_FrontEnd

Backend repository:

https://github.com/EbubekirElicora/Coderr

## Tech Stack

### Backend

- Python 3.12+
- Django 6
- Django REST Framework
- DRF token authentication
- Django Filter
- Django CORS Headers
- Pillow
- SQLite

### Production Deployment

- Google Cloud Compute Engine
- Ubuntu Server
- Gunicorn
- Supervisor
- Nginx
- Let's Encrypt
- Certbot
- HTTPS

## Local Setup

Clone the repository:

```bash
git clone https://github.com/EbubekirElicora/Coderr.git
cd Coderr
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

Create or update the database:

```bash
python manage.py migrate
```

Create an admin user if required:

```bash
python manage.py createsuperuser
```

Start the local development server:

```bash
python manage.py runserver
```

The local API is then available at:

```text
http://127.0.0.1:8000/api/
```

## Demo Login

The deployed frontend provides demo access for both supported user types.

### Demo customer

```text
Username: Demo-Kunde
Password: DemoPassword123!
```

### Demo business user

```text
Username: Demo-Anbieter
Password: DemoPassword123!
```

The demo customer can create orders and reviews.

The demo business user can create offers and update the statuses of orders related to their offers.

Both demo users are normal non-staff accounts. Only staff or superuser accounts can access the Django administration area.

## Django Admin

The local administration area is available at:

```text
http://127.0.0.1:8000/admin/
```

In production it is available below:

```text
https://coderr.ebubekir-elicora.de/admin/
```

Only staff or superuser accounts can access the Django admin.

## Authentication

All protected endpoints use Django REST Framework token authentication.

Header format:

```text
Authorization: Token <token>
```

Login and registration do not require authentication.

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

## User Types

The application supports two profile types:

```text
customer
business
```

Customer users can:

- Create orders
- View their own orders
- Create reviews
- Edit or delete their own reviews

Business users can:

- Create offers
- Edit or delete their own offers
- View orders related to their offers
- Update the status of related orders

## Endpoints

### Authentication

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/api/registration/` | Create a new user profile and return a token |
| POST | `/api/login/` | Authenticate a user and return a token |

### Profiles

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/profile/<user_id>/` | Retrieve one user profile |
| PATCH | `/api/profile/<user_id>/` | Update the authenticated user's own profile |
| GET | `/api/profiles/business/` | List all business profiles |
| GET | `/api/profiles/customer/` | List all customer profiles |

### Offers

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/offers/` | List offers with pagination, filters, search and ordering |
| POST | `/api/offers/` | Create an offer as a business user |
| GET | `/api/offers/<offer_id>/` | Retrieve one offer |
| PATCH | `/api/offers/<offer_id>/` | Update an offer as its owner |
| DELETE | `/api/offers/<offer_id>/` | Delete an offer as its owner |
| GET | `/api/offerdetails/<offerdetail_id>/` | Retrieve one offer detail |

### Orders

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/orders/` | List orders related to the authenticated user |
| POST | `/api/orders/` | Create an order as a customer from an offer detail |
| GET | `/api/orders/<order_id>/` | Retrieve one order |
| PATCH | `/api/orders/<order_id>/` | Update an order status as the related business user |
| DELETE | `/api/orders/<order_id>/` | Delete an order as an admin user |
| GET | `/api/order-count/<business_user_id>/` | Return the active order count for a business user |
| GET | `/api/completed-order-count/<business_user_id>/` | Return the completed order count for a business user |

### Reviews

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/reviews/` | List reviews with filters and ordering |
| POST | `/api/reviews/` | Create a review as a customer |
| PATCH | `/api/reviews/<review_id>/` | Update a review as its owner |
| DELETE | `/api/reviews/<review_id>/` | Delete a review as its owner |

### Base Info

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/base-info/` | Return general marketplace statistics |

## Query Parameters

### Offers

The offer list endpoint supports:

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

The review list endpoint supports:

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

## Response Formats

### Paginated offer response

`GET /api/offers/` returns:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": []
}
```

### Order response

`GET /api/orders/` returns a direct list:

```json
[]
```

### Review response

`GET /api/reviews/` returns a direct list:

```json
[]
```

### Base-info response

The values depend on the current database content.

Example:

```json
{
  "review_count": 2,
  "average_rating": 4.0,
  "business_profile_count": 1,
  "offer_count": 5
}
```

## Permission Rules

- Login, registration, the offer list and base info are publicly accessible.
- All other protected endpoints require token authentication.
- Users can retrieve profile information after authentication.
- Users can only update their own profile.
- Business users can create offers.
- Customer users cannot create offers.
- An offer must contain exactly three offer details.
- Offer detail types within one offer must be unique.
- Only the offer owner can update or delete an offer.
- Authenticated users can retrieve individual offer details.
- Customer users can create orders.
- Business users cannot create orders.
- Orders are created using an `offer_detail_id`.
- Customers can view their own orders.
- Business users can view orders related to their offers.
- Only the related business user can update an order status.
- Only staff or admin users can delete orders.
- Customer users can create reviews.
- Business users cannot create reviews.
- A customer can only create one review per business user.
- Only the review creator can update or delete a review.

## Production Architecture

The deployed application uses the following structure:

```text
Browser
   ↓
Nginx
   ├── /          → Coderr frontend
   ├── /api/      → Gunicorn and Django REST Framework
   ├── /admin/    → Django administration
   ├── /static/   → collected Django static files
   └── /media/    → uploaded media files
```

The backend runs internally through Gunicorn on:

```text
127.0.0.1:8002
```

Port `8002` is not exposed directly to the internet. All public requests are handled by Nginx over HTTPS.

Supervisor keeps the Gunicorn process running and automatically restarts it when required.

## Production Environment Variables

Production settings are passed through the Supervisor configuration.

The following environment variables are used:

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

The real production secret key must never be committed to GitHub.

## Updating the Production Backend

Connect to the server and open the backend directory:

```bash
cd /var/www/projects/coderr/backend
```

Create a database backup before important changes:

```bash
cp db.sqlite3 "db.sqlite3.backup-$(date +%Y%m%d-%H%M%S)"
```

Pull the current repository version:

```bash
git pull
```

Activate the virtual environment:

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

Check its status:

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

## Development Checks

Run the Django system check:

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

Check installed dependencies:

```bash
python -m pip check
```

Update `requirements.txt` on Windows without creating a UTF-16 file:

```powershell
cmd /c "python -m pip freeze > requirements.txt"
```

On Linux or macOS:

```bash
python -m pip freeze > requirements.txt
```

## Project Structure

```text
Coderr/
├── auth_app/
│   └── api/
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── marketplace_app/
│   └── api/
│       ├── views.py
│       └── urls.py
├── offer_app/
│   ├── models.py
│   └── api/
│       ├── permissions.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── order_app/
│   ├── models.py
│   └── api/
│       ├── permissions.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── profile_app/
│   ├── models.py
│   └── api/
│       ├── permissions.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── review_app/
│   ├── models.py
│   └── api/
│       ├── permissions.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Important Rules

- Do not commit `db.sqlite3`.
- Do not commit real production secrets.
- Do not commit `env/`, `venv/` or `.venv/`.
- Do not commit `staticfiles/`.
- Do not commit local media files.
- Do not commit `__pycache__/` directories.
- Keep the backend and frontend in separate repositories.
- Keep `requirements.txt` up to date.
- Run `python manage.py check` before pushing changes.
- Remove debugging `print()` statements before submission.
- Do not commit the frontend into this backend repository.
