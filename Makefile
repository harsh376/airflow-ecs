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
	pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv
