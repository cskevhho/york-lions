from myapp import create_app, extensions, models

app = create_app()

with app.app_context():
    extensions.db.create_all()
