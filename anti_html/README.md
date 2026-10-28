# Anti HTML

## Problem

Write a program that accepts a URL as a command-line argument, downloads the webpage's HTML, strips HTML tags, and prints the remaining text.

## Approach

- Use `argparse` to accept the URL.
- Use `requests` to download the webpage.
- Use Beautiful Soup to parse the HTML and extract readable text.
- Handle unsuccessful HTTP responses.

## Requirements

- Python 3.13 or compatible version
- Requests
- Beautiful Soup 4
- pytest
- Ruff

## Clone the Repository

```powershell
git clone https://github.com/Kaushal1122/Python-Assignment.git
cd Python-Assignment/anti_html
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the Program

```powershell
python -m src.anti_html https://example.com
```

Replace `https://example.com` with the URL you want to process.

## Run Tests

```powershell
python -m pytest -v
```

## Run Ruff

```powershell
python -m ruff check src tests
```