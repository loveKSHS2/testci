install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint app.py

test:
	python -m pytest -vv --cov=app app.py


