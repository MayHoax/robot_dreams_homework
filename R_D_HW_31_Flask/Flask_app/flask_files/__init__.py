from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from logging.config import dictConfig
from .config import AppConfig
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s %(message)s',
    }}
})

app.config.from_object(AppConfig)
db.init_app(app)

from .views import *
from .models import *


with app.app_context():
    db.create_all()
