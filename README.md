# pixel2svgpkg

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/pixel2svgpkg)](https://pypi.org/project/pixel2svgpkg/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pixel2svgpkg)
![PyPI - License](https://img.shields.io/pypi/l/pixel2svgpkg)

A Python package/fork from the [pixel2svg](https://florian-berger.de/en/software/pixel2svg/) project by [Florian Berger](https://florian-berger.de/en/).

## Development

- `poetry install`
- `poetry shell`

## Tech Stack

### Packaging and Development

- [Poetry](https://python-poetry.org/)
- [Mypy](http://mypy-lang.org/)
- [isort](https://pycqa.github.io/isort/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/)
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  - [pep8-naming](https://github.com/PyCQA/pep8-naming)
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [Bandit](https://bandit.readthedocs.io/)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-pkg`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.

## Notes

- Poetry:
  - `poetry --version`.
  - [Licenses](https://python-poetry.org/docs/pyproject#license).
  - [Exception: `No module named 'virtualenv.activation.nushell'`](https://github.com/python-poetry/poetry/issues/4515) issue. Run `poetry self update` to update Poetry (to version 1.1.11).
- VS Code:
  - [Different python.defaultInterpreterPath by workspace not being saved](https://github.com/microsoft/vscode-python/issues/12633#issuecomment-651853209) issue. Set `python.defaultInterpreterPath` instead of `python.pythonPath` in the `settings.json` file. More info [here](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter).
- [ColorSpace](https://mycolor.space/gradient3) (3-Color-Gradient).
- [Gremlins tracker for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=nhoizey.gremlins): to identify characters that can be harmful because they are invisible or look like legitimate ones.
- [pixel2svg-fork](https://github.com/cyChop/pixel2svg-fork).
- [toml](https://github.com/uiri/toml) package. `poetry add --dev toml`.
