
from werkzeug.security import generate_password_hash
from database import connect_db

email = input("Enter student email: ").strip()
new_password = input("Enter new password: ")

connection = connect_db()
cursor = connection.cursor()

password_hash = generate_password_hash(new_password)

cursor.execute(
    """
    UPDATE users
    SET password_hash = %s
    WHERE email = %s AND role = 'Student'
    """,
    (password_hash, email)
)

connection.commit()

if cursor.rowcount > 0:
    print("Student password reset successfully!")
else:
    print("No matching student account found.")

cursor.close()
connection.close()
