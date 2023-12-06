# EECS4413-Project

## Setting up

1. `python -m venv .venv` or `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `export FLASK_APP=yorklions`
5. `flask run --debug`

Or, simply use `setup.sh`.

After initial setup is complete you can use `run.sh` to skip the setup and installation steps, and simply run it.

## Reinitializing database

Everytime we add new models to the schema or edit existing ones, delete your `instance` and `migrations` folders.

1. `flask db init`
2. `flask db migrate`
3. `flask db upgrade`

Or, simply use `reinit_db.sh`.
