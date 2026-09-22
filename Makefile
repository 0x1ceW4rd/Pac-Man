install:
	pip install mazegenerator-00001/mazegenerator-2.1.0-py3-none-any.whl pygame flake8 mypy

run:
	python3 src/main.py

debug:
	python3 -m pdb src/main.py

clean:
	rm -rf .mypy_cache */.mypy_cache
	rm -rf __pycache__ */__pycache__

lint:
	flake8 src/
	mypy src/ --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

