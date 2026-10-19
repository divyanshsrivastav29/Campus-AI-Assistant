
import mysql.connector
from mysql.connector import Error
from config import Config


def connect_db():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return connection

    except Error as error:
        print(f"Database connection failed: {error}")
        return None


if __name__ == "__main__":
    connection = connect_db()

    if connection and connection.is_connected():
        print("Database connection successful!")
        print("Connected database:", connection.database)
        connection.close()
    else:
        print("Could not connect to the database.")
