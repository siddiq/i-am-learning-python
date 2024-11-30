.PHONY: test
test:
	@poetry run pytest -v -s


.PHONY: test-collections
test-collections:
	@poetry run pytest -v -s -k collections


.PHONY: clean
clean:
	@rm -rf .pytest_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} +


.PHONY: install
install:
	@poetry install
