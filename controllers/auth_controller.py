from flask import Blueprint, request, jsonify
from ..services.auth_service import register_user, login_user

auth_app = Blueprint("auth_app", __name__)


@auth_app.post("/register", methods=["POST"])
def register():
    try:
        data = request.json
        email = data["email"]
        password = data["password"]
        pass_repeat = data["pass_repeat"]
        nickname = data["nickname"]

        register_user(email, password, pass_repeat, nickname)

        return jsonify({"message": "User Registered Successfully"}), 201

    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@auth_app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        email = data["email"]
        password = data["password"]

        result = login_user(email, password)

        return jsonify(result), 200

    except ValueError as e:
        return jsonify({"message": str(e)}), 401
