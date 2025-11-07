from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.schemas import ProductSchema
from app import db

bp = Blueprint("product", __name__, url_prefix="/product")


@bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify(ProductSchema(many=True).dump(products))


@bp.route("/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(ProductSchema().dump(product))


@bp.route("/", methods=["POST"])
def add_product():
    product = ProductSchema().load(request.json)
    db.session.add(product)
    db.session.commit()
    return jsonify(ProductSchema().dump(product)), 201


@bp.route("/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get_or_404(id)
    product = ProductSchema(partial=True).load(request.json, instance=product)
    db.session.commit()
    return jsonify(ProductSchema().dump(product))


@bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200
