# Restaurant Kitchen Service 

Django project for managing dishes, dish types and cooks in restaurant

## Check it out!
[Restaurant project deployed to Render](https://restaurant-service-t3pf.onrender.com/)

You can use this data to login:

username: user

password: user12345

## Installation

Python3 must be already installed

```shell
git clone https://github.com/HlovaOleh/kitchen-service
cd kitchen_service
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver  # starts Django Server
```

## Features

* Authentication functionality for Cook/User
* Managing dishes, dish types and cooks directly from website interface
* Powerful admin panel for advanced managing

## Configuration
You can configure the application with the following environment variables:

* SECRET_KEY: is a crucial component of your Django project's security. 
It is used for various cryptographic operations and should be kept confidential. 
Do not share it publicly or expose it in your version control system.
* DEBUG: setting controls whether your Django application is in debug mode. 
In debug mode, detailed error pages are shown, making it easier to identify and fix issues during development. 
However, it's crucial to set `DEBUG` to `False` in production to avoid exposing sensitive information.
* DATABASE_URL: A PostgreSQL connection string, used to connect to the database.
* CSRF_COOKIE_SECURE: Ensures that the CSRF cookie is only sent over HTTPS connections.
* SESSION_COOKIE_SECURE: Ensures that the session cookie is only sent over HTTPS connections.
* SECURE_SSL_REDIRECT: Redirects all non-HTTPS requests to HTTPS.
* SECURE_HSTS_SECONDS: Sets the duration (in seconds) that the browser should remember to only access the site over HTTPS.
* SECURE_HSTS_INCLUDE_SUBDOMAINS: Includes all subdomains when applying HSTS (HTTP Strict Transport Security).
* SECURE_HSTS_PRELOAD: Indicates whether to preload the site in the HSTS preload list maintained by browsers.
* SECURE_CONTENT_TYPE_NOSNIFF: Prevents browsers from interpreting files as a different MIME type than declared by the server.
* 
