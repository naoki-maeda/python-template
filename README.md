# Python Template Repository

Python application template.

Poetry is required to use this template.


## Usage

1. [Install Poetry](https://python-poetry.org/docs/#installation)
2. Setup Virtual Environment And Install Dependency
```
poetry install
```
3. Setup pre-commit
```
poetry run pre-commit install
```
4. Run Test
```
poetry run pytest
```
5. Change tool.poetry and python_template directory.

If you change the python_template directory, please also modify test_init.py.

## Dev Dependencies

- mypy
- black
- flake8
- isort
- pytest
- pre-commit
