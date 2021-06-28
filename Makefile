SHELL := /bin/bash

install:
	python3 -m pip install -r requirements.txt

clean:
	for name in .pytest_cache __pycache__ .vsidea .idea .mypy_cache; do find . -name $$name -exec rm -rf {} \;; done

venv:
	./tiny_python_env/bin/activate
