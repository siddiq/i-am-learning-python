.PHONY: test
test:
	@poetry run pytest -v -s


.PHONY: shell
shell:
	@poetry shell


.PHONY: clean
clean:
	@rm -rf .pytest_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} +


.PHONY: install
install:
	@poetry install
