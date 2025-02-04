from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes import pdf_bp
    app.register_blueprint(pdf_bp)
    
    return app
