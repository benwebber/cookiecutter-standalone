.PHONY: all \
	clean \
	dist \
	help \
	install \
	release \
	rpm \
	sdist \
	standalone \
	wheel

PROJECT := $(shell python setup.py --name)
PACKAGE := $(subst -,_,$(PROJECT))
VERSION := $(shell python setup.py --version)
WHEEL   := $(PACKAGE)-$(VERSION)-py2.py3-none-any.whl

define USAGE
Targets:

  clean       remove build artifacts
  dist        build source distribution and wheel
  install     install package to active Python site packages
  release     build and upload package to PyPI
  rpm         build RPM
  dist        build source distribution
  standalone  build standalone executable .zip
  wheel       build wheel
endef

all: clean dist

help:
	@echo $(info $(USAGE))

clean:
	$(RM) -r build dist
	find . -name '*.pyc' -delete
	find . -name '*.egg-info' -exec $(RM) -r {} +
	find . -name '*.egg' -delete

dist: sdist wheel

install:
	python setup.py install

release: dist
	twine upload dist/*.whl dist/*.tar.gz

standalone: wheel
	scripts/make-standalone.sh $(PROJECT) $(VERSION) $(PACKAGE) $(WHEEL)

rpm: sdist
	scripts/make-rpm.sh $(PROJECT)

sdist: clean
	python setup.py sdist

wheel: clean
	python setup.py bdist_wheel
