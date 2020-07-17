

class SqlGenerator:

    @staticmethod
    def setup_database_queries() -> str:
        for query in [
            """
                PRAGMA foreign_keys = ON;
            """,
            """
                CREATE TABLE IF NOT EXISTS rates_history (
                    id INTEGER PRIMARY KEY,
                    start_from DATE NOT NULL UNIQUE
                );
            """,
            """
                CREATE TABLE IF NOT EXISTS rates (
                    id INTEGER PRIMARY KEY,
                    cargo_type TEXT NOT NULL,
                    rate FLOAT NOT NULL,
                    rate_history_id INTEGER NOT NULL,
                    FOREIGN KEY (rate_history_id)
                    REFERENCES rates_history (id)
                );
            """,
        ]:
            yield query

    @staticmethod
    def get_drop_db_queries():
        for query in [
            """DROP TABLE IF EXISTS rates;""",
            """DROP TABLE IF EXISTS rates_history""",

        ]:
            yield query

    @staticmethod
    def insert_rate(start_from: str) -> str:
        query = f"""
            INSERT INTO rates_history (start_from)
            VALUES ('{start_from}')
        """
        return query

    @staticmethod
    def insert_cargo_rate(history_id: str, cargo_type: str, rate: str) -> str:
        query = f"""
            INSERT INTO rates (cargo_type, rate, rate_history_id)
            VALUES ('{cargo_type}', {rate}, {history_id})
        """
        return query

    @staticmethod
    def get_current_rate_by_cargo_type(cargo_type: str) -> str:
        query = f"""
            SELECT rate
            FROM rates
            JOIN rates_history AS rh ON rates.rate_history_id = rh.id
            WHERE cargo_type='{cargo_type}' ORDER BY start_from desc LIMIT 1;
        """
        return query
