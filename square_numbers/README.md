# Square Numbers Using map() and lambda

## Problem

Write a Python program that uses `map()` and a lambda function to generate a list of squares of numbers from 1 to 20, inclusive.

## Approach

- Use `range(1, 21)` to generate numbers from 1 to 20.
- Use `lambda` to calculate the square of each number.
- Use `map()` to apply the function to every number.
- Convert the result to a list using `list()`.

## Example Output

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
```

## Repository Setup

Clone the repository:

```powershell
git clone https://github.com/Kaushal1122/Python-Assignment.git
```

Navigate to the project directory:

```powershell
cd Python-Assignment/square_numbers
```

## Requirements

- Python 3.13 or compatible version
- pytest
- Ruff

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the Program

```powershell
python -m src.main
```

## Run Tests

```powershell
python -m pytest -v
```

## Run Ruff

```powershell
python -m ruff check src tests
```