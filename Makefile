init:
	pip install -r requirements.txt

test:
	nosetests test

.PHONY: init test