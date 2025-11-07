from . import db
from sqlalchemy import Enum, JSON
from datetime import datetime


class Supplier(db.Model):
    __tablename__ = "supplier"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255))
    phone = db.Column(db.String(50))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Warehouse(db.Model):
    __tablename__ = "warehouse"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text)
    status = db.Column(Enum("active", "inactive"), default="active", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.BigInteger, primary_key=True)
    sku = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


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



# ----------------------------------------------------------------------
# User model for authentication
# ----------------------------------------------------------------------

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """Simple user table used for JWT / OAuth2 authentication."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(32), default="user")   # e.g. "admin", "user"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------
    def set_password(self, password: str) -> None:
        """Hash and store the password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Validate a plain‑text password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User {self.email}>"
