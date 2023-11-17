source .venv/bin/activate
rm -rf instance
rm -rf migrations
export FLASK_APP=yorklions
flask db init
flask db migrate
flask db upgrade
deactivate

