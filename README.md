# Coderr Frontend

Coderr is a marketplace web application where customers can find and order digital services from business users.

This repository contains the frontend of the Coderr project.  
The application communicates with a separate Django REST Framework backend.

## Live Demo

The deployed application is available at:

https://coderr.ebubekir-elicora.de

## Repositories

Frontend:

https://github.com/EbubekirElicora/Coderr_FrontEnd

Backend:

https://github.com/EbubekirElicora/Coderr

## Features

### Authentication

- Customer and business registration
- Login with token authentication
- Guest demo accounts
- Automatic authentication state handling
- Logout functionality

### Profiles

- Customer profiles
- Business profiles
- Public profile details
- Profile editing
- Profile image support
- Business information and contact details

### Offers

- Display available service offers
- Search and filter offers
- Sort offers by price and update date
- Offer pagination
- Detailed offer pages
- Three service packages per offer
- Creation and editing of offers by business users

### Orders

- Customers can create orders
- Customers can view their own orders
- Business users can view orders related to their offers
- Business users can update order statuses
- Completed and active order statistics

### Reviews

- Customers can create reviews
- Reviews can be edited and deleted by their owners
- Business profiles display ratings
- Marketplace statistics show the number and average of reviews

### Legal information

- Privacy policy
- Imprint
- HTTPS encryption
- Information about user accounts, Local Storage and hosting

## Tech Stack

- HTML5
- CSS3
- JavaScript
- Fetch API
- Django REST Framework API
- Token authentication
- Nginx
- Google Cloud Compute Engine
- Let's Encrypt HTTPS

## Project Structure

```text
Coderr_FrontEnd/
├── assets/
├── scripts/
├── shared/
│   ├── scripts/
│   └── styles/
├── styles/
├── business_profile.html
├── customer_profile.html
├── imprint.html
├── index.html
├── login.html
├── offer.html
├── offer_list.html
├── own_profile.html
├── privacy_policy.html
└── registration.html
```

## Local Setup

Clone the repository:

```bash
git clone https://github.com/EbubekirElicora/Coderr_FrontEnd.git
```

Open the project directory:

```bash
cd Coderr_FrontEnd
```

The frontend does not require an additional build process.

Open `index.html` with a local development server, for example with the VS Code extension **Live Server**.

The frontend expects the local backend at:

```text
http://127.0.0.1:8000/api/
```

## API Configuration

The API configuration is located in:

```text
shared/scripts/config.js
```

The frontend automatically distinguishes between local development and the deployed environment.

Local development:

```text
http://127.0.0.1:8000/api/
```

Production:

```text
/api/
```

In production, Nginx forwards all `/api/` requests to the Django backend.

## Demo Login

Demo customer:

```text
Username: Demo-Kunde
Password: DemoPassword123!
```

Demo business user:

```text
Username: Demo-Anbieter
Password: DemoPassword123!
```

The demo customer can create orders and reviews.

The demo business user can create offers and update order statuses related to their offers.

## Authentication Storage

After login, the frontend stores technically necessary authentication information in the browser's Local Storage.

This includes:

```text
Authentication token
User ID
Username
```

The stored information is required to keep the user logged in and to authorize API requests.

No analytics, advertising or marketing cookies are used.

## Backend Communication

Protected API requests use the following header:

```text
Authorization: Token <token>
```

Example:

```javascript
fetch(`${API_BASE_URL}orders/`, {
    headers: {
        Authorization: `Token ${localStorage.getItem('auth-token')}`
    }
});
```

## Production Deployment

The deployed application uses the following structure:

```text
Browser
   ↓
Nginx
   ├── /          → Coderr frontend
   ├── /api/      → Django backend through Gunicorn
   ├── /admin/    → Django admin
   ├── /static/   → Django static files
   └── /media/    → uploaded media files
```

Production components:

- Google Cloud Compute Engine
- Ubuntu Server
- Nginx
- Gunicorn
- Supervisor
- Django REST Framework
- SQLite
- Let's Encrypt / Certbot
- HTTPS

The backend runs internally on:

```text
127.0.0.1:8002
```

It is not exposed directly to the internet. Public requests are handled by Nginx.

## Updating the Deployment

Push frontend changes from the local project:

```bash
git add .
git commit -m "Describe the frontend change"
git push
```

Update the deployed frontend on the server:

```bash
cd /var/www/projects/coderr/frontend
git pull
```

Because the frontend consists of static HTML, CSS and JavaScript files, no build command or service restart is required after a normal frontend update.

## Development Notes

Before pushing changes:

- Test the frontend with the local backend
- Check the browser console for JavaScript errors
- Verify login and logout
- Verify customer and business accounts
- Test offers, orders and reviews
- Test the imprint and privacy policy
- Do not commit credentials or private data

## Origin and License

The frontend is based on the Coderr project template provided by the Developer Akademie and was extended and connected to a separately developed Django REST Framework backend as part of the backend course.

The original license information is retained in:

```text
LICENSE.md
```