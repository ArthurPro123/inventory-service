from . import ma
from .models import Supplier, Warehouse, Product, ProductVariant, Inventory, User


class SupplierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        load_instance = True


class WarehouseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Warehouse
        load_instance = True


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True


class ProductVariantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductVariant
        load_instance = True


class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        load_instance = True
        include_fk = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
