# Remove Duplicates from a List

## Problem

Given a list of numbers, remove all duplicate values while preserving their original order.

## Example

**Input:**
```python
[12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
```

**Output:**
```python
[12, 24, 35, 88, 120, 155]
```

## Approach

Use a set to track numbers that have already appeared and a list to store unique numbers in their original order.

## Repository Setup

Clone the repository:

```powershell
git clone https://github.com/Kaushal1122/Python-Assignment.git
```

Navigate to the project directory:

```powershell
cd Python-Assignment/remove_duplicates
```

## Requirements

- Python 3.13 or compatible version
- pytest
- Ruff

## Installation

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
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

## Code Quality Checks

```powershell
python -m ruff check src tests
```