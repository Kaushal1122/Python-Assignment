
import logging
import sys

from src.config import ConfigurationError
from src.database import DatabaseConnectionError
from src.record_generator import generate_records

logger = logging.getLogger(__name__)

QUERY = """
    SELECT emp_no, first_name, last_name
    FROM employees
    ORDER BY emp_no
"""

DISPLAY_LIMIT = 10


def main():
    processed_count = 0

    try:
        for record in generate_records(QUERY):
            processed_count += 1

            if processed_count <= DISPLAY_LIMIT:
                print(record)

        logger.info(
            "Processing completed. Total records processed: %d",
            processed_count,
        )
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
