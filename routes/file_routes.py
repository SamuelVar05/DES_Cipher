from flask import Blueprint, request, send_file, jsonify
from controllers.file_controller import handle_encrypt, handle_decrypt

file_routes = Blueprint("file_routes", __name__)

@file_routes.route("/encrypt", methods=["POST"])
def encrypt_route():
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file = request.files["file"]
    user_key = request.form.get("key")

    if not user_key:
        return jsonify({"error": "Debe enviar la clave"}), 400

    output_path = handle_encrypt(file, user_key)
    return send_file(output_path, as_attachment=True)


@file_routes.route("/decrypt", methods=["POST"])
def decrypt_route():
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file = request.files["file"]
    user_key = request.form.get("key")

    if not user_key:
        return jsonify({"error": "Debe enviar la clave"}), 400

    output_path = handle_decrypt(file, user_key)
    return send_file(output_path, as_attachment=True)

