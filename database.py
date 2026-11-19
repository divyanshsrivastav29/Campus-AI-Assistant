import mysql.connector
from mysql.connector import Error
from config import Config
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CA_PATH = BASE_DIR / "ca.pem"


def connect_db(database=None):
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=database or Config.DB_NAME,
            ssl_ca=str(CA_PATH),
            ssl_verify_cert=True,
            ssl_verify_identity=True,
            connection_timeout=20,
            use_pure=True
        )
        return connection

    except Error as error:
        print(f"Database connection failed: {error}")
        return None


if __name__ == "__main__":
    connection = connect_db()

    if connection and connection.is_connected():
        print("TiDB connection successful!")
        print("Connected database:", connection.database)
        connection.close()
    else:
        print("Could not connect to TiDB.")
