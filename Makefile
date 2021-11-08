.PHONY: all check type isort black lint bandit

CMD:=poetry run
PYMODULE:=pixel2svgpkg

all: check type isort black lint bandit

check:
	poetry check

type:
	$(CMD) mypy $(PYMODULE)

isort:
	$(CMD) isort $(PYMODULE)

black:
	$(CMD) black $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE)

bandit:
	$(CMD) bandit -r $(PYMODULE)
