from .. import db
from datetime import datetime
from sqlalchemy import JSON

class ProductVariant(db.Model):
    __tablename__ = "product_variant"
    id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey("product.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    extra_json = db.Column(JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    product = db.relationship("Product", backref="variants")
