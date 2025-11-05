import pytest
from app import create_app
from app.models import Supplier
from app import db


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
    return app


def test_supplier_creation(app):
    with app.app_context():
        supplier = Supplier(name="Test Supplier")
        db.session.add(supplier)
        db.session.commit()
        assert Supplier.query.count() == 1
