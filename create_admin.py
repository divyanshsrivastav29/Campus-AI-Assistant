
import getpass
import mysql.connector
from werkzeug.security import generate_password_hash
from database import connect_db


def create_admin():
    name = input("Admin full name: ").strip()
    email = input("Admin email: ").strip().lower()
    password = getpass.getpass("Create admin password: ")
    confirm = getpass.getpass("Confirm password: ")

    if not name or not email or not password:
        print("All fields are required.")
        return

    if password != confirm:
        print("Passwords do not match.")
        return

    if len(password) < 10:
        print("Use a password with at least 10 characters.")
        return

    connection = connect_db()
    if connection is None:
        print("Database connection failed.")
        return

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT user_id FROM users WHERE email = %s",
            (email,)
        )

        if cursor.fetchone():
            print("This email is already registered.")
            return

        password_hash = generate_password_hash(password)

        cursor.execute(
            """
            INSERT INTO users
                (full_name, email, password_hash, role)
            VALUES (%s, %s, %s, 'Admin')
            """,
            (name, email, password_hash)
        )

        connection.commit()
        print("Admin account created successfully!")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Could not create admin:", error)

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_admin()
