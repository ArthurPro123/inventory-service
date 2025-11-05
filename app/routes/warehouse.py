from flask import Blueprint, request, jsonify
from app.models import Warehouse
from app.schemas import WarehouseSchema
from app import db

bp = Blueprint("warehouse", __name__, url_prefix="/warehouse")


@bp.route("/", methods=["GET"])
def get_warehouses():
    warehouses = Warehouse.query.all()
    return jsonify(WarehouseSchema(many=True).dump(warehouses))


@bp.route("/<int:id>", methods=["GET"])
def get_warehouse(id):
    warehouse = Warehouse.query.get_or_404(id)
    return jsonify(WarehouseSchema().dump(warehouse))


@bp.route("/", methods=["POST"])
def add_warehouse():
    warehouse = WarehouseSchema().load(request.json)
    db.session.add(warehouse)
    db.session.commit()
    return jsonify(WarehouseSchema().dump(warehouse)), 201


@bp.route("/<int:id>", methods=["PUT"])
def update_warehouse(id):
    warehouse = Warehouse.query.get_or_404(id)
    warehouse = WarehouseSchema(partial=True).load(request.json, instance=warehouse)
    db.session.commit()
    return jsonify(WarehouseSchema().dump(warehouse))


@bp.route("/<int:id>", methods=["DELETE"])
def delete_warehouse(id):
    warehouse = Warehouse.query.get_or_404(id)
    db.session.delete(warehouse)
    db.session.commit()
    return jsonify({"message": "Warehouse deleted"}), 200
