.PHONY: venv bin clean link copy rm-wu

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

link:
	@sudo ln -sv "$$(pwd)/wu" /usr/local/bin/wu

copy:
	@sudo cp -v wu /usr/local/bin 

rm-wu:
	@sudo rm -rfv /usr/local/bin/wu
