check:
	rm -rf .tox
	tox -e mypy
	tox -e flake8 
	tox -e pylint
	tox

lint:
	rm -rf .tox
	tox -e flake8
	tox -e pylint

mypy:
	rm -rf .tox
	tox -e mypy

test:
	rm -rf .tox
	tox
