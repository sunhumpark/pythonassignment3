# main.py
"""
Updated main program for feature-update branch.
Includes improved input validation.
"""
from file_handler import load_records, save_records
from grade_calc import calculate_student_grade, view_records

def main():
    records = load_records()

    while True:
        print("\n--- Student Grade Calculator ---")
        print("1. Enter new student grades")
        print("2. View saved records")
        print("3. Exit")

        choice = input("Choose: ").strip()
        if choice not in ["1", "2", "3"]:
            print("Invalid option. Please enter 1, 2, or 3.")
            continue

        if choice == "1":
            result = calculate_student_grade()
            records.append(result)
            save_records(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


# file_handler.py
import os

FILE_NAME = "grades.txt"

def load_records():
    records = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                records.append(line.strip())
    return records

def save_records(records):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for r in records:
            file.write(r + "\n")


# grade_calc.py
"""
Feature-update: Added strong input validation for score entry.
"""

def calculate_student_grade():
    name = input("Student name: ").strip()

    # number of subjects validation
    while True:
        try:
            count = int(input("Number of subjects: "))
            if count <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid number. Please enter a valid integer.")

    marks = []

    # score validation added (new feature)
    for i in range(count):
        while True:
            try:
                score = float(input(f"Score for subject {i+1}: "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    total = sum(marks)
    average = total / count

    # grade calculation
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    result = f"{name} | Total: {total} | Average: {average:.2f} | Grade: {grade}"

    print("\n=== Result ===")
    print(result)

    return result

def view_records(records):
    print("\n--- Saved Records ---")
    if len(records) == 0:
        print("No records found.")
    else:
        for i in range(len(records)):
            print(records[i])