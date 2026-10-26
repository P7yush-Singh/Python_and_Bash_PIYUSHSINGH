students = {
    "Rahul": "A",
    "Priya": "B",
    "PIYUSH": "C"
}

while True:
    print("Student Grades Menu")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Display all student grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists.")
        else:
            grade = input("Enter grade: ").upper()
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            grade = input("Enter new grade: ").upper()
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nStudent Grades:")

        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
