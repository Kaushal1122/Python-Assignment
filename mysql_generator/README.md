# MySQL Employee Record Generator

A Python application that retrieves employee records from a MySQL database using generators to process large datasets incrementally and reduce memory usage.

## Features

- Retrieves database records incrementally using a Python generator.
- Uses an unbuffered MySQL cursor to avoid buffering the complete result set.
- Manages database connections and cursors with proper cleanup.
- Loads database settings from a configuration file.
- Reads the database password from an environment variable.
- Includes logging and exception handling.
- Includes unit tests using `pytest`.
- Uses Ruff for code quality and PEP 8-related checks.

## Project Structure

```text
mysql_generator/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── record_generator.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_database.py
│   ├── test_record_generator.py
│   └── test_main.py
├── config.ini
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.15
- MySQL Server 8.0 or a compatible version
- Git
- The MySQL Employees sample database

## Installation

### 1. Clone the repository

Clone this project from GitHub, then navigate to the project directory:

```powershell
git clone https://github.com/Kaushal1122/Python-Assignment.git
cd mysql_generator
```


### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Database Setup

This project uses the MySQL Employees sample database from the official [datacharmer/test_db repository](https://github.com/datacharmer/test_db).

### 1. Download the sample database

Clone the sample database repository:

```powershell
git clone https://github.com/datacharmer/test_db.git
cd test_db
```

Keep `employees.sql` and its associated `.dump` files together in the downloaded directory. The SQL script uses these files while loading the data.

### 2. Import the database

Ensure your MySQL Server is running. From the directory containing `employees.sql` and the `.dump` files, execute:

```powershell
cmd /c '"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p -t < employees.sql'
```

Enter your MySQL root password when prompted.

The command above assumes MySQL Server 8.0 is installed in the default Windows directory. If MySQL is installed elsewhere, update the path to `mysql.exe`.

### 3. Verify the database

Connect to MySQL:

```powershell
mysql -u root -p
```

Then execute:

```sql
USE employees;
SHOW TABLES;
SELECT COUNT(*) FROM employees;
```

The standard dataset contains approximately 300,000 employee records. The expected employee count is **300,024**.

For additional setup details and troubleshooting, refer to the [official test_db README](https://github.com/datacharmer/test_db/blob/master/README.md).

## Configuration

Update `config.ini` with your local MySQL connection settings:

```ini
[database]
host = localhost
port = 3306
database = employees
user = root

[processing]
batch_size = 1000
```

Set the database password through the `MYSQL_PASSWORD` environment variable in PowerShell:

```powershell
$env:MYSQL_PASSWORD = "your_mysql_password"
```

Replace the placeholder with your actual password. Do not commit passwords or other secrets to Git.

## Run the Application

From the project root, run:

```powershell
python -m src.main
```

The application retrieves employee records incrementally, prints the first 10 records, and logs the total number of records processed.

## Run Unit Tests

Execute the test suite with:

```powershell
python -m pytest -v
```

The tests cover configuration validation, database connection handling, incremental record retrieval, resource cleanup, and application behavior.

The tests use mocks where appropriate, so they do not all require a live MySQL connection.

## Code Quality

Run Ruff to check the source code and tests:

```powershell
python -m ruff check src tests
```

Ruff settings are defined in `pyproject.toml`.

## Implementation Notes

- The generator uses `fetchone()` with an unbuffered cursor to retrieve records incrementally.
- The database connection and cursor are closed when processing finishes or the generator is stopped.
- Database credentials are kept outside the source code using an environment variable.
- The configured `batch_size` is validated, but the current implementation retrieves records one at a time rather than in batches.
- The application prints only the first 10 records but continues processing the full query result.

## License and Dataset Attribution

The sample database is maintained by the [datacharmer/test_db project](https://github.com/datacharmer/test_db). Refer to its repository for dataset licensing, attribution, and disclaimer information.

This repository is a Python learning assignment focused on clean code, generators, database access, logging, exception handling, configuration, and unit testing.