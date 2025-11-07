from flask import Blueprint, request, jsonify
from app.models.supplier import Supplier
from app.schemas import SupplierSchema
from app import db

bp = Blueprint("supplier", __name__, url_prefix="/supplier")


@bp.route("/", methods=["GET"])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify(SupplierSchema(many=True).dump(suppliers))


@bp.route("/<int:id>", methods=["GET"])
def get_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    return jsonify(SupplierSchema().dump(supplier))


@bp.route("/", methods=["POST"])
def add_supplier():
    supplier = SupplierSchema().load(request.json)
    db.session.add(supplier)
    db.session.commit()
    return jsonify(SupplierSchema().dump(supplier)), 201


@bp.route("/<int:id>", methods=["PUT"])
def update_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    supplier = SupplierSchema(partial=True).load(request.json, instance=supplier)
    db.session.commit()
    return jsonify(SupplierSchema().dump(supplier))


@bp.route("/<int:id>", methods=["DELETE"])
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({"message": "Supplier deleted"}), 200
