python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=yorklions
flask run --debug

