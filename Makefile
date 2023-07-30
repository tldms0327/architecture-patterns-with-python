.PHONY: install
install:
	poetry install --no-root

.PHONY: update
update:
	poetry update

.PHONY: lint
lint:
	poetry run pre-commit install && poetry run pre-commit run

.PHONY: lint-update
lint-update:
	poetry run pre-commit autoupdate
