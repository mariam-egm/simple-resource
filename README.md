# DjangoRest API Project

## Overview
This project is a DjangoRest API for managing products. It includes CRUD (Create, Read, Update, Delete) operations for a **Product** model.

## Features
**Create:** Add new products with a name and description.
**Read:** Retrieve a list of products or view details of a specific product.
**Update:** Modify the details of an existing product.
**Delete:** Remove a product from the database.

## Installation
1- Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
```
2- Apply migrations:
```
python manage.py migrate
```
3- Run the development server:
```
python manage.py runserver
```
4- Access the API at **http://127.0.0.1:8000/resource/**


## Usage
- **List resources**: `GET /resource`
- **Get a resource by id:** `GET /resource/{id}`
- **Create a resource:** `POST /resource`
- **Update a resource:** `PATCH /resource/{id}`
- **Delete a resource:** `DELETE /resource/{id}`

## Testing
Run unit tests using the following command:
```
python manage.py test products.tests
```

