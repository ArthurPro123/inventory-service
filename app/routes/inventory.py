from flask import Blueprint, request, jsonify
from app.models.inventory import Inventory
from app.schemas import InventorySchema
from app import db

# -----------------------------------------------------------
from flask_jwt_extended import jwt_required, get_jwt_identity
# -----------------------------------------------------------



bp = Blueprint("inventory", __name__, url_prefix="/inventory")

@bp.route("/", methods=["GET"])
@jwt_required()
def get_inventories():
    inventories = Inventory.query.all()
    return jsonify(InventorySchema(many=True).dump(inventories))


@bp.route("/<int:id>", methods=["GET"])
def get_inventory(id):
    inventory = Inventory.query.get_or_404(id)
    return jsonify(InventorySchema().dump(inventory))


@bp.route("/", methods=["POST"])
def add_inventory():
    try:
        inventory = InventorySchema().load(request.json)
        db.session.add(inventory)
        db.session.commit()
        return jsonify(InventorySchema().dump(inventory)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@bp.route("/<int:id>", methods=["PUT"])
def update_inventory(id):
    inventory = Inventory.query.get_or_404(id)
    inventory = InventorySchema(partial=True).load(request.json, instance=inventory)
    db.session.commit()
    return jsonify(InventorySchema().dump(inventory))


@bp.route("/<int:id>", methods=["DELETE"])
def delete_inventory(id):
    inventory = Inventory.query.get_or_404(id)
    db.session.delete(inventory)
    db.session.commit()
    return jsonify({"message": "Inventory deleted"}), 200


@bp.route("/query", methods=["GET"])
def inventory_query():
    query = """
    SELECT
        p.sku,
        p.name AS product_name,
        pv.name AS variant_name,
        w.code AS warehouse,
        s.name AS supplier,
        i.quantity_on_hand,
        i.quantity_reserved,
        i.cost_price,
        i.retail_price
    FROM inventory AS i
    JOIN product AS p ON p.id = i.product_id
    LEFT JOIN product_variant AS pv ON pv.id = i.variant_id
    JOIN warehouse AS w ON w.id = i.warehouse_id
    JOIN supplier AS s ON s.id = i.supplier_id
    ORDER BY p.sku, pv.id, w.code
    """
    result = db.session.execute(query)
    rows = result.fetchall()
    return jsonify([dict(row) for row in rows])
