# Person Gender

A Python assignment demonstrating inheritance and abstract classes using Python's built-in `abc` module.

## Features

- Defines an abstract `Person` class.
- Declares `get_gender()` as an abstract method.
- Implements `Male` and `Female` subclasses.
- Prevents direct instantiation of the abstract `Person` class.
- Includes unit tests using pytest.
- Uses Ruff for code linting.

## Project Structure

```text
person_gender/
├── src/
│   ├── __init__.py
│   └── person.py
├── tests/
│   ├── __init__.py
│   └── test_person.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.15 or a compatible Python version.
- Git.

## Setup

### 1. Clone the repository

```powershell
git clone https://github.com/Kaushal1122/Python-Assignment.git
cd Python-Assignment/person_gender
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Usage

The `Person` class is abstract and cannot be instantiated directly. The `Male` and `Female` classes inherit from `Person` and implement the abstract `get_gender()` method.

Example:

```python
from src.person import Female, Male

male = Male()
female = Female()

print(male.get_gender())
print(female.get_gender())
```

Output:

```text
Male
Female
```

Attempting to instantiate `Person` directly raises a `TypeError`:

```python
from src.person import Person

person = Person()
```

## Run Tests

Execute the unit tests using pytest:

```powershell
python -m pytest -v
```

The tests verify that:

- `Male().get_gender()` returns `"Male"`.
- `Female().get_gender()` returns `"Female"`.
- Instantiating `Person` raises `TypeError`.

## Run Linting

Check the source code and tests using Ruff:

```powershell
python -m ruff check src tests
```

## Technologies Used

- Python
- Abstract Base Classes (`abc`)
- pytest
- Ruff

## Learning Objectives

- Understand class inheritance in Python.
- Implement abstract classes and abstract methods.
- Enforce method implementation in subclasses.
- Write unit tests for class behavior.
- Maintain consistent code quality through linting.