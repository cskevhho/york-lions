# EECS4413-Project

## Setting up

1. `python -m venv .venv` or `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `export FLASK_APP=yorklions`
5. `flask run --debug`

## Reinitializing server

If you choose to delete the instance folder to just quickly refresh your current database (can probably delete the migrations file too for a fresh run).:

1. `flask db init`
2. `flask db migrate`
3. `flask db upgrade`

## Other things

1. Use `sqlite3 instance/db.sqlite3` to access db schema and tables with `.schema` and `.tables`.
2. User is just a demo/example model to base our model prototyping off of.
