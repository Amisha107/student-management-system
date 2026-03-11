import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
roll TEXT,
course TEXT
)
""")

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students(name,roll,course) VALUES(?,?,?)",(name,roll,course))
    conn.commit()
    print("Student added successfully\n")


def display_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    for row in data:
        print(row)


def search_student():
    roll = input("Enter roll number: ")
    cursor.execute("SELECT * FROM students WHERE roll=?",(roll,))
    data = cursor.fetchone()

    if data:
        print(data)
    else:
        print("Student not found")


def delete_student():
    roll = input("Enter roll number to delete: ")
    cursor.execute("DELETE FROM students WHERE roll=?",(roll,))
    conn.commit()
    print("Student deleted")


while True:

    print("\n----- Student Management System -----")
    print("1 Add Student")
    print("2 Display Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid choice")