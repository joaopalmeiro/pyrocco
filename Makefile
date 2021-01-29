.PHONY: init clean-build clean-img clean

init:
	export PIPENV_VENV_IN_PROJECT=1 && \
	pipenv install --python 3.8 --dev

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-img:
	rm -f *.png
	rm -f *.gif

clean: clean-img clean-build
