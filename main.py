'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import re

FILE_NAME = "students.txt"


def validate_email(email):
    """Return True if the email has a valid basic format."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email) is not None


def save_student(student):
    """Append one student record to the text file."""
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{student['id']},{student['name']},{student['email']}\n")


def read_students():
    """Read and return all student records from the file."""
    students = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",", 2)
                if len(parts) == 3:
                    students.append({
                        "id": parts[0],
                        "name": parts[1],
                        "email": parts[2]
                    })

    except FileNotFoundError:
        # The file will be created automatically when the first student is added.
        pass

    return students


def add_student():
    """Get student details, validate them, and save the record."""
    try:
        student_id = int(input("Enter Student ID: "))

        if student_id <= 0:
            raise ValueError("Student ID must be a positive number.")

        name = input("Enter Student Name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        email = input("Enter Email: ").strip()

        if not validate_email(email):
            print("Invalid email format. Student was not added.")
            return

        # Prevent duplicate student IDs.
        existing_students = read_students()
        if any(student["id"] == str(student_id) for student in existing_students):
            print("Student ID already exists. Student was not added.")
            return

        student = {
            "id": student_id,
            "name": name,
            "email": email
        }

        save_student(student)
        print("Student added successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")


def display_students():
    """Display all saved student records."""
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")
    for student in students:
        print(f"ID    : {student['id']}")
        print(f"Name  : {student['name']}")
        print(f"Email : {student['email']}")
        print("-" * 30)


def main():
    """Run the Student Record Manager menu."""
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                display_students()
            elif choice == 3:
                print("Thank you for using Student Record Manager!")
                break
            else:
                print("Please enter a choice between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
