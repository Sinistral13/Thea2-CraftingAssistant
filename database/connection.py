import psycopg2
import os
from dotenv import load_dotenv


class DatabaseConnection:

    def __init__(self):
        load_dotenv()

        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))

    def close(self):
        self.connection.close()