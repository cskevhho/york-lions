from myapp import create_app, extensions
from myapp.models import *

app = create_app()

with app.app_context():
    extensions.db.create_all()
