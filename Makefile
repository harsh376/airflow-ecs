.PHONY: help
.DEFAULT: help
help:
	@echo "make install"
	@echo "	updates existing environment"
	@echo "make clean"
	@echo "	deletes venv"

venv: requirements.txt
	test -d venv || python3 -m venv venv

.PHONY: install
install:
	make venv; \
	. venv/bin/activate; \
	pip install invoke; \
	invoke unset-hooks; \
	invoke install

.PHONY: clean
clean:
	rm -rf venv

# This command is so that pre-commit can run a local command
.PHONY: black
black:
	. venv/bin/activate; \
	invoke black


.PHONY: docformatter
docformatter:
	. venv/bin/activate; \
	invoke docformatter
