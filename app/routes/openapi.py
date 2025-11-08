from flask import send_from_directory
import os

def init_specs_routes(app):
    @app.route("/specs/openapi.json")
    def serve_openapi():
        specs_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/" + "specs"
        return send_from_directory(specs_dir, "openapi.json")
