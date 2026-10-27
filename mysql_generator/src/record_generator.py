
import logging

from src.database import get_connection

logger = logging.getLogger(__name__)


def generate_records(query, params=None):
    with get_connection() as connection:
        cursor = connection.cursor(buffered=False)

        try:
            cursor.execute(query, params or ())
            logger.info("SQL query executed successfully.")

            while True:
                record = cursor.fetchone()

                if record is None:
                    break

                yield record

        finally:
            cursor.close()
            logger.info("Database cursor closed.")
