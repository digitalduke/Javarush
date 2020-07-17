import json
import sqlite3
from json.decoder import JSONDecodeError
from sys import (
    stderr,
    stdout,
)

from nnst.db.builders import SqlGenerator


DATABASE_NAME = 'nnst.db'


class DbManager:

    @staticmethod
    def setup_db():
        with sqlite3.connect(DATABASE_NAME) as connection:
            for query in SqlGenerator.setup_database_queries():
                stdout.write(f"Executing query: {query}\n")
                connection.execute(query)

    @staticmethod
    def fill_db(path: str):
        try:
            with open(path) as json_data:
                raw_data = json.load(json_data)
        except JSONDecodeError:
            stderr.write('Error: exception while processing JSON file')
            exit(1)

        with sqlite3.connect(DATABASE_NAME) as connection:
            for rate_date, rates_info in raw_data.items():
                query = SqlGenerator.insert_rate(rate_date)
                stdout.write(f"Executing query: {query}\n")
                response = connection.execute(query)
                rate_history_id = response.lastrowid

                for rate_info in rates_info:
                    query = SqlGenerator.insert_cargo_rate(
                        history_id=rate_history_id,
                        cargo_type=rate_info['cargo_type'],
                        rate=rate_info['rate'],
                    )
                    stdout.write(f"Executing query: {query}\n")
                    connection.execute(query)

    @staticmethod
    def drop_db():
        with sqlite3.connect(DATABASE_NAME) as connection:
            for query in SqlGenerator.get_drop_db_queries():
                stdout.write(f"Executing query: {query}\n")
                connection.execute(query)
