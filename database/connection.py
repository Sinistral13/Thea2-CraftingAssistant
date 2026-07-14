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
            
        self.connection = fdb.connect(
            dsn="THEA_MAT",
            user="SYSDBA",
            password=db_password
            )

            
        
    def close(self):
        self.connection.close()