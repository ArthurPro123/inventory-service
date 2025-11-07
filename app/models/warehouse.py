from .. import db
from datetime import datetime
from sqlalchemy import Enum

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
