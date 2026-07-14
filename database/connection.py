import fdb
import os
from dotenv import load_dotenv


class DatabaseConnection:

    def __init__(self):
        load_dotenv()

        db_password = os.getenv("DB_PASSWORD")

        if not db_password:
            raise ValueError(
                "DB_PASSWORD not found. Please add your DB_PASSWORD to the .env file."
            )

        db_path = os.path.join(
            os.path.dirname(__file__),
            "THEA_MAT.fdb"
        )

        self.connection = fdb.connect(
            database=db_path,
            user="SYSDBA",
            password=db_password
        )

            
        
    def close(self):
        self.connection.close()