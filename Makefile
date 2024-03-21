clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
build:
	python setup.py bdist_wheel