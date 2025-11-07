from flask import Blueprint, request, jsonify
from app.models.product_variant import ProductVariant
from app.schemas import ProductVariantSchema
from app import db

bp = Blueprint("product_variant", __name__, url_prefix="/product_variant")


@bp.route("/", methods=["GET"])
def get_product_variants():
    variants = ProductVariant.query.all()
    return jsonify(ProductVariantSchema(many=True).dump(variants))


@bp.route("/<int:id>", methods=["GET"])
def get_product_variant(id):
    variant = ProductVariant.query.get_or_404(id)
    return jsonify(ProductVariantSchema().dump(variant))


@bp.route("/", methods=["POST"])
def add_product_variant():
    variant = ProductVariantSchema().load(request.json)
    db.session.add(variant)
    db.session.commit()
    return jsonify(ProductVariantSchema().dump(variant)), 201


@bp.route("/<int:id>", methods=["PUT"])
def update_product_variant(id):
    variant = ProductVariant.query.get_or_404(id)
    variant = ProductVariantSchema(partial=True).load(request.json, instance=variant)
    db.session.commit()
    return jsonify(ProductVariantSchema().dump(variant))


@bp.route("/<int:id>", methods=["DELETE"])
def delete_product_variant(id):
    variant = ProductVariant.query.get_or_404(id)
    db.session.delete(variant)
    db.session.commit()
    return jsonify({"message": "Product variant deleted"}), 200
