
build:
	python setup.py sdist

clean:
	rm -rf dist/ build/ Vaka_Avto.egg-info

.PHONY: clean build