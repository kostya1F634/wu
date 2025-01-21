.PHONY: venv bin clean

all: venv bin

venv:
	@python3 -m venv venv
	@./venv/bin/pip install -r requirements.txt

bin:
	@./venv/bin/pyinstaller --onefile --clean src/wu.py
	@mv dist/wu ./
	@rm -rf build
	@rm -rf dist
	@rm -rf wu.spec

clean:
	@rm -rf venv
	@rm -rf build
	@rm -rf dist
	@rm -rf wu.spec


