# Student Management System in Python
# Works on Mobile (Pydroid 3)

import os

FILE_NAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age},{course}\n")

    print("✅ Student added successfully!\n")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("⚠️ No student data available.\n")
    else:
        print("\n📋 Student Records:")
        print("-" * 40)
        for student in students:
            roll, name, age, course = student.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Age: {age} | Course: {course}")
        print("-" * 40)

def search_student():
    roll = input("Enter Roll Number to Search: ")

    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found!\n")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            student_roll, name, age, course = line.strip().split(",")
            if student_roll == roll:
                print("\n✅ Student Found:")
                print(f"Roll: {student_roll}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Course: {course}\n")
                found = True
                break

    if not found:
        print("❌ Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    new_list = []
    deleted = False

    for student in students:
        student_roll = student.split(",")[0]
        if student_roll != roll:
            new_list.append(student)
        else:
            deleted = True

    with open(FILE_NAME, "w") as file:
        file.writelines(new_list)

    if deleted:
        print("✅ Student deleted successfully!\n")
    else:
        print("❌ Student not found!\n")

def main_menu():
    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("✅ Exiting Program. Thank you!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

main_menu()