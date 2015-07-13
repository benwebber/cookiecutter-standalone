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

NAME	:= $(shell python setup.py --name)
VERSION := $(shell python setup.py --version)
WHEEL	:= $(subst -,_,$(NAME))-$(VERSION)-py2.py3-none-any.whl

all: clean dist

help:
	@echo 'Targets:'
	@echo
	@echo '  clean       remove build artifacts'
	@echo '  dist        build source distribution and wheel'
	@echo '  install     install package to active Python site packages'
	@echo '  release     build and upload package to PyPI'
	@echo '  rpm         build RPM'
	@echo '  dist        build source distribution'
	@echo '  standalone  build standalone executable .zip'
	@echo '  wheel       build wheel'

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
	scripts/make-standalone.sh $(NAME) $(WHEEL)

rpm: sdist
	scripts/make-rpm.sh $(NAME)

sdist: clean
	python setup.py sdist

wheel: clean
	python setup.py bdist_wheel