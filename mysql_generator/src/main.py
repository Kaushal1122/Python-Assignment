import logging
import sys

from src.config import ConfigurationError
from src.database import DatabaseConnectionError
from src.record_generator import generate_records

logger = logging.getLogger(__name__)

DISPLAY_LIMIT = 10

QUERIES = {
    "SELECT - Employee Details": """
        SELECT emp_no, first_name, last_name
        FROM employees
        ORDER BY emp_no
    """,
    "WHERE - Filter Employees": """
        SELECT emp_no, first_name, last_name
        FROM employees
        WHERE emp_no < %s
        ORDER BY emp_no
    """,
    "ORDER BY - Sort Employees": """
        SELECT emp_no, first_name, last_name
        FROM employees
        ORDER BY first_name ASC
    """,
    "LIMIT - First 10 Employees": """
        SELECT emp_no, first_name, last_name
        FROM employees
        ORDER BY emp_no
        LIMIT 10
    """,
    "DISTINCT - Unique First Names": """
        SELECT DISTINCT first_name
        FROM employees
        ORDER BY first_name
    """,
    "COUNT - Total Employees": """
        SELECT COUNT(*) AS total_employees
        FROM employees
    """,
    "GROUP BY - Employees by Hire Year": """
        SELECT YEAR(hire_date) AS hire_year,
               COUNT(*) AS employee_count
        FROM employees
        GROUP BY YEAR(hire_date)
        ORDER BY hire_year
    """,
}


QUERY_PARAMS = {
    "WHERE - Filter Employees": (10010,),
}


def execute_query(title, query):
    logger.info("Executing query: %s", title)

    processed_count = 0

    params = QUERY_PARAMS.get(title)

    for record in generate_records(query, params):
        processed_count += 1

        if processed_count <= DISPLAY_LIMIT:
            print(record)

    logger.info(
        "Query completed. Total records processed: %d",
        processed_count,
    )


def main():
    try:
        for title, query in QUERIES.items():
            print(f"\n{'=' * 60}")
            print(title)
            print("=" * 60)

            execute_query(title, query)

        logger.info("All queries executed successfully.")
        return 0

    except (ConfigurationError, DatabaseConnectionError) as exc:
        logger.error("Application failed: %s", exc)
        return 1


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    sys.exit(main())
