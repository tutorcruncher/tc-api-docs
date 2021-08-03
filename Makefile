.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: format
format:
	isort scripts/ extensions.py
	black -S -l 120 --target-version py38 scripts/ extensions.py

.PHONY: lint
lint:
	isort --check-only scripts/ extensions.py
	flake8 scripts/ extensions.py
