from typing import TypedDict


class Student(TypedDict):
    name: str
    id: str
    scores: list[float]


def add_student(students: list[Student]) -> None:
    name = input("Student name: ")
    student_id = input("Student ID: ")

    while True:
        try:
            num_scores = int(input("How many scores? "))
            if num_scores < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative integer.")

    scores: list[float] = []
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Please enter a valid number for the score.")

    student: Student = {
        "name": name,
        "id": student_id,
        "scores": scores,
    }

    students.append(student)
    print(f'Student "{name}" added successfully.')


# Function to display all students
def display_students(students: list[Student]) -> None:
    if not students:
        print("No student records found.")
        return

    print("\n---------------------------------------------------------------")
    print("Name\t\tID\t\tScores\t\tAverage")
    print("---------------------------------------------------------------")

    for student in students:
        scores = student["scores"]
        if scores:
            average = round(sum(scores) / len(scores), 2)
            score_list = ", ".join(str(score) for score in scores)
        else:
            average = "N/A"
            score_list = "No scores"

        print(f"{student['name']}\t{student['id']}\t{score_list}\t{average}")

    print("---------------------------------------------------------------")


# Function to calculate the average score of one student
def calculate_average(students: list[Student]) -> None:
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            scores = student["scores"]
            if not scores:
                print(f"{student['name']} has no scores recorded.")
                return

            average = round(sum(scores) / len(scores), 2)
            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: Student ID not found.")


# Main Program
students: list[Student] = []

while True:
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        calculate_average(students)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please enter a number from 1 to 4.")
