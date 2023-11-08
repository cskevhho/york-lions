from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# this file exists to ease coupling issues with imports

db = SQLAlchemy()
migrate = Migrate()