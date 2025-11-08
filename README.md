# Inventory Management API


**Project Overview**
This is my **end-to-end personal project**: a **Flask-based REST API** for
managing inventory, products, suppliers, and warehouses. Designed for
scalability and ease of integration, this API supports core inventory
operations with secure authentication and detailed OpenAPI documentation.


**Goals**
- Provide a robust backend for inventory management systems.
- Ensure secure access to protected endpoints using JWT authentication.
- Offer API contract via OpenAPI.

---

## Features
- **CRUD Operations**: Full support for suppliers, warehouses, products, variants, and inventory.
- **Relationships**: Models are linked using Foreign Keys and one-to-many relationships.
- **Authentication**: JWT-based protection for POST, PUT, and DELETE endpoints.
- **OpenAPI Support**: Detailed OpenAPI specification for API contract validation.

---

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **Containerization**: Docker Compose
- **API Testing**: Postman, cURL

---

## Prerequisites
- Docker Compose
- Git
- API client (Postman, curl)

---

## Setup

### 1. Clone the Repository
```sh
git clone https://github.com/ArthurPro123/inventory-service.git
cd inventory-service
```

### 2. Build and start the containers:
```sh
make build
make run
```

The API will be available at http://localhost:5000.


### (*). Stop the API:
```sh
make stop
```

---

## Authentication

### Protected Endpoints
- All POST, PUT, and DELETE endpoints require JWT authentication.


### Login endpoint
- URL: /auth/login
- Method: POST


### Testing Credentials
- Email: `admin@example.com`
- Password: `SuperSecret123`


#### Example: Login with cURL
```sh
curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@example.com", "password": "SuperSecret123"}'
```

---

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
|                 | `/inventory/query`      | GET              | Fetch detailed inventory data        |
|                 |                         |                  |                                      | 
| **OpenAPI**     | `/specs/openapi.json`   | GET              | Access the OpenAPI specification     |


---

## OpenAPI Specification

### Purpose

The OpenAPI endpoint provides a machine-readable specification of the API,
including:

- All available routes
- Request/response schemas
- Authentication methods
- Example payloads


### Usage

- Validate API requests and responses against the contract using tools like
  Swagger UI.

---

## Example API Requests

### 1. List All Suppliers
```sh
curl -X GET http://localhost:5000/supplier \
     -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```

### 2. Create a New Product
```sh
curl -X POST http://localhost:5000/product \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <YOUR_JWT_TOKEN>" \
     -d '{"name": "New Product", "description": "Product description"}'
```

### 3. Fetch Detailed Inventory Data
```sh
curl -X GET http://localhost:5000/inventory/query \
     -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```

---

## Additional Notes

- **Environment Variables**: All required environment variables are configured
  in the Makefile. No additional setup is needed unless you customize the
  deployment.
- This project was developed independently. While contributions are not
  actively solicited, feedback and suggestions are always welcome. 
