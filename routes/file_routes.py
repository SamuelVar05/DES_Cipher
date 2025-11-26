from flask import Blueprint, request, send_file
from controllers.file_controller import handle_encrypt, handle_decrypt

file_routes = Blueprint("file_routes", __name__)

@file_routes.route("/encrypt", methods=["POST"])
def encrypt_route():
    file = request.files["file"]
    output_path = handle_encrypt(file)
    return send_file(output_path, as_attachment=True)

@file_routes.route("/decrypt", methods=["POST"])
def decrypt_route():
    file = request.files["file"]
    output_path = handle_decrypt(file)
    return send_file(output_path, as_attachment=True)
