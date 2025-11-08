from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()




def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # ---- JWT setup --------------------------------------------------
    from flask_jwt_extended import JWTManager
    import os

    # Use a strong secret – keep it out of source control (env var)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "fallback‑insecure‑key")

    # Optional: look for JWT in request headers:
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]  

    # Optional: token expiration, refresh token handling, etc:
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600   # 1 hour

    # Optional: refresh token expires in 1 day:
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 86400

    # Initialize JWTManager
    jwt = JWTManager(app)

    from .routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    # -----------------------------------------------------------------

    db.init_app(app)
    ma.init_app(app)

    # #
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()



    # Import and register blueprints:
    from app.routes import main, supplier, warehouse, product, product_variant, inventory

    app.register_blueprint(main.bp)
    app.register_blueprint(supplier.bp)
    app.register_blueprint(warehouse.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(product_variant.bp)
    app.register_blueprint(inventory.bp)


    # Register the openapi route:
    from app.routes.openapi import init_specs_routes
    init_specs_routes(app)

    return app
