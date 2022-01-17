from flask import Flask
import os
from . import db

def create_app():
    # existing code omitted
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'EMS.db'),
        
    ))
    return app