install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C api.py

test:
	python -m pytest -vv --cov=api app.py


