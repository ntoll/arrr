XARGS := xargs -0 $(shell test $$(uname) = Linux && echo -r)
GREP_T_FLAG := $(shell test $$(uname) = Linux && echo -T)
export PYFLAKES_BUILTINS=_

all:
	@echo "\nThere is no default Makefile target right now. Try:\n"
	@echo "make clean - reset the project and remove auto-generated assets."
	@echo "make tidy - tidy code with the 'black' formatter."
	@echo "make docs - use Sphinx to create project documentation."
	@echo "make dist- package up Arrr."
	@echo "make publish-test - upload Arrr to the test PyPI instance."
	@echo "make publish-live - uplaod Arrr to the main PyPI instance."

clean:
	rm -rf arrr.egg-info
	rm -rf .pytest_cache
	rm -rf docs/_build
	rm -rf .eggs
	rm -rf build
	rm -rf dist
	find . \( -name '*.py[co]' -o -name dropin.cache \) -delete
	find . \( -name '*.bak' -o -name dropin.cache \) -delete
	find . \( -name '*.tgz' -o -name dropin.cache \) -delete
	find . | grep -E "(__pycache__)" | xargs rm -rf

tidy: clean
	@echo "\nTidying code with black..."
	black -l 79 arrr.py 

docs: clean
	$(MAKE) -C docs html
	@echo "\nDocumentation can be found here:"
	@echo file://`pwd`/docs/_build/html/index.html
	@echo "\n"

dist: clean
	@echo "\nChecks pass, good to package..."
	python setup.py sdist bdist_wheel

publish-test: dist
	@echo "\nPackaging complete... Uploading to PyPi..."
	twine upload -r test --sign dist/*

publish-live: dist
	@echo "\nPackaging complete... Uploading to PyPi..."
	twine upload --sign dist/*
