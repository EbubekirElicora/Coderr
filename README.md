# Coderr Backend API

This repository contains the Django REST Framework backend for the Coderr frontend.  
All documented API endpoints are available below `/api/`.

## Tech stack

- Python 3.12+
- Django
- Django REST Framework
- Token authentication
- Django Filter
- Django CORS Headers
- Pillow
- SQLite for local development

## Setup

Create a virtual environment:

```bash
python -m venv env
```

Windows PowerShell:

```bash
.\env\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Create an admin user if needed:

```bash
python manage.py createsuperuser
```

Run the backend:

```bash
python manage.py runserver
```

The API is then available at:

```text
http://127.0.0.1:8000/api/
```

## Django admin

The admin area is available at:

```text
http://127.0.0.1:8000/admin/
```

Only staff or superuser accounts can access the Django admin.

## Authentication

All protected endpoints use DRF token authentication.

Header format:

```text
Authorization: Token <token>
```

Login and registration do not require authentication.

## User types

The application supports two profile types:

```text
customer
business
```

Customer users can create orders and reviews.  
Business users can create offers and update related order statuses.

## Endpoints

### Authentication

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/api/registration/` | Create a new user profile and return a token |
| POST | `/api/login/` | Login and return a token |

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
| POST | `/api/offers/` | Create an offer as business user |
| GET | `/api/offers/<offer_id>/` | Retrieve one offer |
| PATCH | `/api/offers/<offer_id>/` | Update an offer as owner |
| DELETE | `/api/offers/<offer_id>/` | Delete an offer as owner |
| GET | `/api/offerdetails/<offerdetail_id>/` | Retrieve one offer detail |

### Orders

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/orders/` | List orders related to the authenticated user |
| POST | `/api/orders/` | Create an order as customer user from an offer detail |
| GET | `/api/orders/<order_id>/` | Retrieve one order |
| PATCH | `/api/orders/<order_id>/` | Update an order status as related business user |
| DELETE | `/api/orders/<order_id>/` | Delete an order as admin user |
| GET | `/api/order-count/<business_user_id>/` | Return active order count for a business user |
| GET | `/api/completed-order-count/<business_user_id>/` | Return completed order count for a business user |

### Reviews

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/reviews/` | List reviews with filters and ordering |
| POST | `/api/reviews/` | Create a review as customer user |
| PATCH | `/api/reviews/<review_id>/` | Update a review as owner |
| DELETE | `/api/reviews/<review_id>/` | Delete a review as owner |

### Base Info

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/base-info/` | Return marketplace statistics |

## Query parameters

### Offers

The offer list endpoint supports the following query parameters:

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

### Reviews

The review list endpoint supports the following query parameters:

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

## Permission rules

- Anonymous users can only use login, registration, offer list and base info.
- Protected endpoints require the following header: `Authorization: Token <token>`.
- Users can retrieve profile data.
- Users can only update their own profile.
- Business users can create offers.
- Customer users cannot create offers.
- An offer must contain exactly three offer details.
- Offer detail types must be unique.
- Only the offer owner can update or delete an offer.
- Authenticated users can retrieve offer details.
- Customer users can create orders.
- Business users cannot create orders.
- Orders are created from an `offer_detail_id`.
- Customers can see their own orders.
- Business users can see orders related to their offers.
- Only the related business user can update an order status.
- Only admin users can delete orders.
- Customer users can create reviews.
- Business users cannot create reviews.
- A customer can only create one review per business user.
- Only the review creator can update or delete their review.

## Response examples

### Authentication response

```json
{
  "token": "example-token",
  "username": "business_user",
  "email": "business@test.de",
  "user_id": 2
}
```

### Base info response

```json
{
  "review_count": 0,
  "average_rating": 0,
  "business_profile_count": 1,
  "offer_count": 1
}
```

## Development checks

Run the Django system check before submission:

```bash
python manage.py check
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create or update dependencies:

```bash
pip freeze > requirements.txt
```

## Project structure

```text
coderr_backend/
├── auth_app/
│   └── api/
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── core/
│   ├── settings.py
│   └── urls.py
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

## Important rules

- Do not commit `db.sqlite3`.
- Do not commit `env/`, `venv/` or `.venv/`.
- Do not commit `__pycache__/` folders.
- Do not commit local media files.
- Keep the backend in its own repository.
- Keep `requirements.txt` up to date.
- Run `python manage.py check` before submission.
- Remove all `print()` statements before submission.
- The frontend must not be committed into this backend repository.