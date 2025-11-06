# Inventory Management API

This project demonstrates a Flask-based REST API for managing inventory, products, suppliers, and warehouses.

---

## Features
- CRUD operations for suppliers, warehouses, products, variants, and inventory.
 - Relationships between models (Foreign Keys, one-to-many, etc.)
 - Custom query endpoint for complex inventory reports.

## Setup

1. Clone the Repository
```
git clone <repo-url>
cd inventory-service
```

2. Install Dependencies
```
pip install -r requirements txt
```

## Docker

1. Build and start the containers:
```
docker compose up --build
```

<!--
```
export FLASK_APP=app.py
flask run
```
-->

2. The API will be available at http://localhost:5000.

3. To stop: 
````
docker compose down
```

---

## API Endpoints

| Resource        | Endpoint                | Methods          | Description                          |
|-----------------|-------------------------|-----------       |--------------------------------------|
| **Suppliers**   | `/supplier`             | GET, POST        | List/create suppliers                |
|                 | `/supplier/<id>`        | GET, PUT, DELETE | Manage a supplier                    |
| **Warehouses**  | `/warehouse`            | GET, POST        | List/create warehouses               |
|                 | `/warehouse/<id>`       | GET, PUT, DELETE | Manage a warehouse                   |
| **Products**    | `/product`              | GET, POST        | List/create products                 |
|                 | `/product/<id>`         | GET, PUT, DELETE | Manage a product                     |
| **Variants**    | `/product_variant`      | GET, POST        | List/create product variants         |
|                 | `/product_variant/<id>` | GET, PUT, DELETE | Manage a variant                     |
| **Inventory**   | `/inventory`            | GET, POST        | List/create inventory items          |
|                 | `/inventory/<id>`       | GET, PUT, DELETE | Manage an inventory item             |

---

## Testing
Run the tests with:
````
pytest tests/
```
