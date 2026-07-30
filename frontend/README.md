# Coderr Frontend

This directory contains the frontend of the Coderr full-stack marketplace application.

Coderr allows customers to discover and order digital services from business users. The frontend communicates with a Django REST Framework backend located in the same monorepo.

---

## Live Deployment

### Application

https://coderr.ebubekir-elicora.de/

### Public API Example

https://coderr.ebubekir-elicora.de/api/base-info/

### Repository

https://github.com/EbubekirElicora/Coderr

### Backend Source

[`../backend/`](../backend/)

---

## Project Overview

The Coderr frontend provides the user interface for the marketplace application.

It supports two different user types:

- Customers
- Business users

Customers can browse offers, create demo orders and review business users.

Business users can create service offers and manage orders related to their offers.

The frontend is built without a JavaScript framework and uses:

- HTML
- CSS
- Vanilla JavaScript
- Fetch API
- Browser Local Storage
- Django REST Framework API

No frontend build process is required.

---

## Features

### Authentication

- Customer registration
- Business-user registration
- Login with token authentication
- Guest demo accounts
- Automatic authentication-state handling
- Logout functionality
- Protected API requests
- Local Storage integration
- User-type-dependent navigation

### Profiles

- Customer profiles
- Business profiles
- Public profile details
- Profile editing
- Profile-image support
- Business descriptions
- Location information
- Contact details
- Working-hours information
- User-type-dependent profile views

### Offers

- Display available service offers
- Search offers
- Filter offers
- Sort offers by price
- Sort offers by update date
- Paginated offer lists
- Detailed offer pages
- Three service packages per offer
- Basic, standard and premium packages
- Offer creation by business users
- Offer editing by owners
- Offer deletion by owners
- Delivery-time information
- Revision information
- Individual service features

### Orders

- Customers can create demo orders
- Customers can view their own orders
- Business users can view orders related to their offers
- Business users can update related order statuses
- Active-order statistics
- Completed-order statistics
- Order data loaded through the REST API
- No real payment processing

### Reviews

- Customers can review business users
- Rating selection
- Review descriptions
- Reviews can be edited by their owners
- Reviews can be deleted by their owners
- Business profiles display ratings
- Marketplace statistics display review counts
- Marketplace statistics display average ratings

### Legal and Privacy Information

- Imprint
- Privacy policy
- Information about user accounts
- Information about Local Storage
- Information about hosting
- HTTPS encryption
- No analytics cookies
- No advertising cookies
- No marketing tracking

---

## Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- Browser Local Storage
- Responsive design
- Static HTML pages

### Backend Communication

- Django REST Framework
- REST API
- JSON
- DRF Token Authentication
- Multipart form data for image uploads

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

- Visual Studio Code
- Live Server
- Git
- GitHub
- Browser Developer Tools
- Postman
- Windows PowerShell

---

## Project Structure

```text
frontend/
├── assets/
│   ├── icons/
│   ├── img/
│   └── ...
│
├── scripts/
│   └── ...
│
├── shared/
│   ├── scripts/
│   │   ├── config.js
│   │   └── ...
│   └── styles/
│       └── ...
│
├── styles/
│   └── ...
│
├── business_profile.html
├── customer_profile.html
├── imprint.html
├── index.html
├── login.html
├── offer.html
├── offer_list.html
├── own_profile.html
├── privacy_policy.html
├── registration.html
├── CHANGELOG.md
├── LICENSE.md
└── README.md
```

---

## Application Pages

### Home Page

```text
index.html
```

The home page presents the marketplace and displays general statistics.

It can include information such as:

- Number of business profiles
- Number of offers
- Number of reviews
- Average rating

The values are loaded from:

```text
GET /api/base-info/
```

### Login

```text
login.html
```

Provides:

- User login
- Demo-customer access
- Demo-business-user access
- Token storage
- Authentication-state handling

### Registration

```text
registration.html
```

Supports registration for:

```text
customer
business
```

### Offer List

```text
offer_list.html
```

Provides:

- Offer overview
- Search
- Filters
- Sorting
- Pagination
- Navigation to offer details

### Offer Detail

```text
offer.html
```

Displays:

- Offer information
- Business-user information
- Basic package
- Standard package
- Premium package
- Prices
- Delivery times
- Revisions
- Included features
- Order functionality

### Customer Profile

```text
customer_profile.html
```

Displays customer-profile information.

### Business Profile

```text
business_profile.html
```

Displays:

- Business information
- Description
- Contact details
- Location
- Working hours
- Ratings
- Reviews
- Related offers

### Own Profile

```text
own_profile.html
```

Allows authenticated users to:

- View their own profile
- Edit profile information
- Upload or update a profile image
- Manage user-type-specific information

### Imprint

```text
imprint.html
```

Contains the legal provider information for the portfolio project.

### Privacy Policy

```text
privacy_policy.html
```

Contains information about:

- User accounts
- Authentication
- Local Storage
- Server hosting
- Uploaded profile data
- HTTPS encryption
- No analytics or advertising cookies

---

## Local Setup

Clone the complete monorepo:

```bash
git clone https://github.com/EbubekirElicora/Coderr.git
```

Open the frontend directory:

```bash
cd Coderr/frontend
```

The frontend does not require:

- npm
- Node.js
- a package installation
- a build command
- a compilation step

Open `index.html` using a local development server.

A recommended option is the Visual Studio Code extension:

```text
Live Server
```

Do not open the HTML file only through the local file system when testing API communication.

Use a local HTTP server instead.

---

## Local Backend

The frontend expects the local backend at:

```text
http://127.0.0.1:8000/api/
```

Before starting the frontend locally, start the Django backend from the `backend` directory:

```bash
cd ../backend
```

Activate the virtual environment on Windows:

```powershell
.\env\Scripts\Activate.ps1
```

Start Django:

```bash
python manage.py runserver
```

Then start the frontend through Live Server.

---

## API Configuration

The API configuration is located in:

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

In production, the frontend and backend use the same domain.

Nginx forwards requests below `/api/` to the Django backend.

Example:

```text
https://coderr.ebubekir-elicora.de/api/offers/
```

---

## Authentication

The backend uses Django REST Framework token authentication.

A successful login or registration returns an authentication token and basic user information.

Example response:

```json
{
  "token": "example-token",
  "username": "business_user",
  "email": "business@test.de",
  "user_id": 2
}
```

Protected API requests use the following header:

```text
Authorization: Token <token>
```

Example request:

```javascript
fetch(`${API_BASE_URL}orders/`, {
    headers: {
        Authorization: `Token ${localStorage.getItem("auth-token")}`
    }
});
```

---

## Authentication Storage

After a successful login, the frontend stores technically necessary authentication information in the browser's Local Storage.

Depending on the frontend implementation, the stored values include information such as:

```text
Authentication token
User ID
Username
User type
```

These values are used to:

- Keep the user logged in
- Identify the authenticated user
- Display user-specific navigation
- Authorize protected API requests
- Distinguish customer and business accounts

Authentication information is removed during logout.

No analytics, advertising or marketing cookies are used.

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
- Open offer details
- Create demo orders
- View their own orders
- Create reviews
- Edit their own reviews
- Delete their own reviews

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

Both demo accounts are normal non-staff accounts.

They cannot access Django Admin.

---

## Backend Communication

The frontend communicates with the backend using the Fetch API.

### Public Request Example

```javascript
fetch(`${API_BASE_URL}offers/`)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }

        return response.json();
    })
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        console.error(error);
    });
```

### Protected Request Example

```javascript
const token = localStorage.getItem("auth-token");

fetch(`${API_BASE_URL}orders/`, {
    headers: {
        Authorization: `Token ${token}`
    }
})
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }

        return response.json();
    })
    .then((orders) => {
        console.log(orders);
    })
    .catch((error) => {
        console.error(error);
    });
```

### POST Request Example

```javascript
const token = localStorage.getItem("auth-token");

fetch(`${API_BASE_URL}orders/`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`
    },
    body: JSON.stringify({
        offer_detail_id: 1
    })
})
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }

        return response.json();
    })
    .then((order) => {
        console.log(order);
    })
    .catch((error) => {
        console.error(error);
    });
```

---

## Important API Endpoints

### Authentication

```text
POST /api/registration/
POST /api/login/
```

### Profiles

```text
GET   /api/profile/<user_id>/
PATCH /api/profile/<user_id>/
GET   /api/profiles/business/
GET   /api/profiles/customer/
```

### Offers

```text
GET    /api/offers/
POST   /api/offers/
GET    /api/offers/<offer_id>/
PATCH  /api/offers/<offer_id>/
DELETE /api/offers/<offer_id>/
GET    /api/offerdetails/<offerdetail_id>/
```

### Orders

```text
GET    /api/orders/
POST   /api/orders/
GET    /api/orders/<order_id>/
PATCH  /api/orders/<order_id>/
DELETE /api/orders/<order_id>/
```

### Order Statistics

```text
GET /api/order-count/<business_user_id>/
GET /api/completed-order-count/<business_user_id>/
```

### Reviews

```text
GET    /api/reviews/
POST   /api/reviews/
PATCH  /api/reviews/<review_id>/
DELETE /api/reviews/<review_id>/
```

### Marketplace Statistics

```text
GET /api/base-info/
```

Complete API documentation is available in:

[`../backend/README.md`](../backend/README.md)

---

## Offer Search and Filters

The offer-list endpoint supports query parameters such as:

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
/api/offers/?search=design
/api/offers/?min_price=100
/api/offers/?max_delivery_time=5
/api/offers/?ordering=min_price
/api/offers/?ordering=-min_price
/api/offers/?ordering=updated_at
/api/offers/?ordering=-updated_at
/api/offers/?page_size=6
```

The frontend uses these parameters to implement:

- Search fields
- Price filters
- Delivery-time filters
- Sorting controls
- Pagination

---

## User Roles

### Customer

A customer can:

- Browse offers
- View offer details
- Create orders
- View their own orders
- Create reviews
- Edit their own reviews
- Delete their own reviews
- Edit their own profile

### Business User

A business user can:

- Create offers
- Edit their own offers
- Delete their own offers
- View orders related to their offers
- Update related order statuses
- Edit their own profile

The frontend adjusts available buttons, navigation items and actions according to the authenticated user's role.

Backend permissions remain authoritative.

Hiding a button in the frontend is not considered a security mechanism.

---

## Error Handling

The frontend handles API responses based on their HTTP status.

Common status codes include:

```text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
500 Internal Server Error
```

The frontend should:

- Check `response.ok`
- Display understandable error messages
- Avoid exposing internal server information
- Redirect unauthenticated users when required
- Remove invalid authentication data when necessary
- Log development errors to the browser console

Example:

```javascript
if (response.status === 401) {
    localStorage.removeItem("auth-token");
    window.location.href = "login.html";
}
```

---

## Image Uploads

Profile images and other uploaded files are sent to the backend using multipart form data.

Example:

```javascript
const formData = new FormData();

formData.append("first_name", firstName);
formData.append("last_name", lastName);
formData.append("file", imageFile);

fetch(`${API_BASE_URL}profile/${userId}/`, {
    method: "PATCH",
    headers: {
        Authorization: `Token ${token}`
    },
    body: formData
});
```

When using `FormData`, the browser sets the multipart `Content-Type` header automatically.

Do not manually set:

```text
Content-Type: multipart/form-data
```

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

Production components:

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

The backend runs internally on:

```text
127.0.0.1:8002
```

The internal Gunicorn port is not exposed directly to the internet.

Public requests are handled by Nginx.

---

## Production Paths

The complete monorepo is deployed at:

```text
/var/www/projects/coderr
```

Frontend:

```text
/var/www/projects/coderr/frontend
```

Backend:

```text
/var/www/projects/coderr/backend
```

Gunicorn logs:

```text
/var/www/projects/coderr/logs
```

---

## Updating the Production Frontend

Commit and push frontend changes locally:

```bash
git add frontend
git commit -m "Describe the frontend change"
git push origin main
```

Connect to the server and open the monorepo:

```bash
cd /var/www/projects/coderr
```

Pull the latest version:

```bash
git pull
```

The frontend consists of static HTML, CSS and JavaScript files.

A normal frontend-only update does not require:

- dependency installation
- compilation
- a build command
- a Gunicorn restart

After an update, test the public application:

```bash
curl -I https://coderr.ebubekir-elicora.de/
```

When backend files were also changed, follow the backend deployment instructions:

[`../backend/README.md`](../backend/README.md)

---

## Development Checklist

Before committing frontend changes:

- Test the home page
- Test registration
- Test customer registration
- Test business registration
- Test login
- Test logout
- Test demo accounts
- Test authentication persistence
- Test customer navigation
- Test business navigation
- Test profile editing
- Test profile-image uploads
- Test offer lists
- Test search
- Test filters
- Test sorting
- Test pagination
- Test offer details
- Test order creation
- Test customer orders
- Test business orders
- Test order-status updates
- Test review creation
- Test review editing
- Test review deletion
- Test the imprint
- Test the privacy policy
- Check all internal links
- Check the browser console
- Test responsive layouts
- Test the deployed application
- Do not commit credentials or private data

---

## Browser Developer Tools

During frontend development, use the browser developer tools to inspect:

### Console

Check for:

- JavaScript errors
- Undefined variables
- Failed API requests
- Authentication errors

### Network

Check:

- Request URL
- HTTP method
- Request headers
- Authentication token
- Request body
- Response status
- Response body
- CORS errors

### Application

Check Local Storage values such as:

```text
Authentication token
User information
User ID
User type
```

Remove stale authentication values when testing different accounts.

---

## Security Notes

The frontend must not contain:

- Django secret keys
- Server passwords
- SSH keys
- Database files
- Private API credentials
- Personal access tokens
- Unnecessary personal information

Security-relevant permissions are enforced by the backend.

Frontend visibility rules improve the user experience but do not replace server-side authorization.

Production traffic is encrypted using HTTPS.

---

## Accessibility and Responsive Design

The frontend should be tested for:

- Desktop displays
- Tablets
- Mobile devices
- Keyboard navigation
- Form labels
- Button descriptions
- Sufficient contrast
- Readable text sizes
- Meaningful alternative text
- Clear validation messages

Responsive behavior should be checked through the browser's device toolbar and on real devices when possible.

---

## Privacy

The frontend stores technically necessary authentication information in Local Storage.

The project does not use:

- Analytics services
- Advertising networks
- Marketing cookies
- User-tracking platforms

Additional information is available in:

```text
privacy_policy.html
```

---

## Origin and License

The frontend is based on the Coderr project template provided by the Developer Akademie.

It was extended, connected to a separately implemented Django REST Framework backend and deployed as a complete full-stack portfolio project.

The original frontend license information is retained in:

```text
LICENSE.md
```

---

## Related Documentation

### Main Project Documentation

[`../README.md`](../README.md)

### Backend Documentation

[`../backend/README.md`](../backend/README.md)