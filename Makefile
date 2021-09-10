black = black -S -l 120
isort = isort -w 120

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: format
format:
	$(isort) scripts/ extensions.py
	$(black) scripts/ extensions.py

.PHONY: lint
lint:
	flake8 scripts/ extensions.py
	$(isort) --check-only scripts/ extensions.py
	$(black) --check scripts/ extensions.py
