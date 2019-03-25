.PHONY: build
build:
	echo "Clean dist directory"
	rm -f dist/*

	echo "Build dists"
	python3 setup.py sdist

.PHONY: testpypi
testpypi:
	echo "Upload to testpypi"
	twine upload --repository testpypi dist/*

.PHONY: pypi
pypi:
	echo "Upload to pypi"
	twine upload --repository pypi dist/*
