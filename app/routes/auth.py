from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash
from app.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Bad credentials"}), 401

    # Convert user.id to a string
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify(
        access_token=access_token,
        refresh_token=refresh_token,
        user_id=user.id,
    ), 200


# -----------------------------------------------
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)  # Only accepts refresh tokens
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=str(current_user))
    return jsonify(access_token=new_access_token), 200
# -----------------------------------------------
