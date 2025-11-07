from .. import db
from datetime import datetime
from sqlalchemy import Enum

class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey("product.id"), nullable=False)
    variant_id = db.Column(db.BigInteger, db.ForeignKey("product_variant.id"))
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"), nullable=False)
    supplier_id = db.Column(db.BigInteger, db.ForeignKey("supplier.id"))
    quantity_on_hand = db.Column(db.Integer, default=0, nullable=False)
    quantity_reserved = db.Column(db.Integer, default=0, nullable=False)
    cost_price = db.Column(db.Numeric(12, 4))
    retail_price = db.Column(db.Numeric(12, 4))
    currency_code = db.Column(db.String(3), default="USD")
    status = db.Column(
        Enum("active", "inactive", "discontinued"), default="active", nullable=False
    )
    last_stock_update = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    product = db.relationship("Product")
    variant = db.relationship("ProductVariant")
    warehouse = db.relationship("Warehouse")
    supplier = db.relationship("Supplier")
