requirements:
	pipenv lock -r > requirements.txt

install-requirements:
	pip install -r requirements.txt
