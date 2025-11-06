from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return jsonify({
        "message": "Welcome to the Inventory Management API",
        "status": "ok",
        "version": "1.0",
        "documentation": {
            "description": "This API provides endpoints for managing products, warehouses, suppliers, product variants, and inventory.",
            "endpoints": {
                "products": {
                    "url": "/product",
                    "methods": ["GET", "POST"],
                    "description": "Manage product resources."
                },
                "product_by_id": {
                    "url": "/product/<int:id>",
                    "methods": ["GET", "PUT", "DELETE"],
                    "description": "Manage a specific product by ID."
                },
                "warehouses": {
                    "url": "/warehouse",
                    "methods": ["GET", "POST"],
                    "description": "Manage warehouse resources."
                },
                "warehouse_by_id": {
                    "url": "/warehouse/<int:id>",
                    "methods": ["GET", "PUT", "DELETE"],
                    "description": "Manage a specific warehouse by ID."
                },
                "suppliers": {
                    "url": "/supplier",
                    "methods": ["GET", "POST"],
                    "description": "Manage supplier resources."
                },
                "supplier_by_id": {
                    "url": "/supplier/<int:id>",
                    "methods": ["GET", "PUT", "DELETE"],
                    "description": "Manage a specific supplier by ID."
                },
                "product_variants": {
                    "url": "/product_variant",
                    "methods": ["GET", "POST"],
                    "description": "Manage product variant resources."
                },
                "product_variant_by_id": {
                    "url": "/product_variant/<int:id>",
                    "methods": ["GET", "PUT", "DELETE"],
                    "description": "Manage a specific product variant by ID."
                },
                "inventory": {
                    "url": "/inventory",
                    "methods": ["GET", "POST"],
                    "description": "Manage inventory resources."
                },
                "inventory_by_id": {
                    "url": "/inventory/<int:id>",
                    "methods": ["GET", "PUT", "DELETE"],
                    "description": "Manage a specific inventory record by ID."
                }
            }
        }
    })
