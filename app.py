from flask import Flask
from routes.file_routes import file_routes
import os

app = Flask(__name__)

# Crear carpetas
for folder in ["uploads", "uploads/encrypted", "uploads/decrypted"]:
    if not os.path.exists(folder):
        os.makedirs(folder)

app.register_blueprint(file_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
