import fdb
import os
from dotenv import load_dotenv


class DatabaseConnection:

    def __init__(self):
        load_dotenv()

        db_password = os.getenv("DB_PASSWORD")
        firebird_host = os.getenv("FIREBIRD_HOST")

        if not db_password:
            raise ValueError("DB_PASSWORD not found")

        if not firebird_host:
            raise ValueError("FIREBIRD_HOST not found")

        self.connection = fdb.connect(
            host=firebird_host,
            database="/firebird/data/THEA_MAT.FDB",
            user="SYSDBA",
            password=db_password
        )

        print("Connected to Firebird:", firebird_host)


    def close(self):
        self.connection.close()