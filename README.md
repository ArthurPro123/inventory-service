# Inventory Management API

This project demonstrates a Flask-based REST API for managing inventory, products, suppliers, and warehouses.


## Features
- CRUD operations for suppliers, warehouses, products, variants, and inventory.
- Relationships between models (Foreign Keys, one-to-many, etc.)
- JWT-based authentication system to use protected endpoints


## Prerequisites
- Docker Compose
- Git
- API client (Postman, curl)

## Setup

1. Clone the Repository
```sh
git clone https://github.com/ArthurPro123/inventory-service.git
cd inventory-service
```

2. Build and start the containers:
```
make build
make run
```

The API will be available at http://localhost:5000.


## To stop: 
```
make stop
```

## Authentication

- POST, PUT, and DELETE endpoints are protected with JWT authentication
- Login endpoint available at /auth/login

### Testing Credentials
- Email: `admin@example.com`
- Password: `SuperSecret123`

#### Authentication Example for Testing
```sh
# Using curl to login
curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@example.com", "password": "SuperSecret123"}'
```

## API Endpoints

| Resource        | Endpoint                | Methods          | Description                          |
|-----------------|-------------------------|------------------|--------------------------------------|
| **Auth**        | `/auth/login`           | POST             | User authentication                  |
|                 |                         |                  |                                      | 
| **Suppliers**   | `/supplier`             | GET, POST        | List/create suppliers                |
|                 | `/supplier/<id>`        | GET, PUT, DELETE | Manage a supplier                    |
|                 |                         |                  |                                      | 
| **Warehouses**  | `/warehouse`            | GET, POST        | List/create warehouses               |
|                 | `/warehouse/<id>`       | GET, PUT, DELETE | Manage a warehouse                   |
|                 |                         |                  |                                      | 
| **Products**    | `/product`              | GET, POST        | List/create products                 |
|                 | `/product/<id>`         | GET, PUT, DELETE | Manage a product                     |
|                 |                         |                  |                                      | 
| **Variants**    | `/product_variant`      | GET, POST        | List/create product variants         |
|                 | `/product_variant/<id>` | GET, PUT, DELETE | Manage a variant                     |
|                 |                         |                  |                                      | 
| **Inventory**   | `/inventory`            | GET, POST        | List/create inventory items          |
|                 | `/inventory/<id>`       | GET, PUT, DELETE | Manage an inventory item             |
|                 | `/inventory/query`      | GET              | Fetch the detailed inventory data    |

