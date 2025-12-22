# 🌟 Exercise 1 : Student Grade Summary
# Instructions
# You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.

# Initial Data:

# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }

# Requirements:
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
# Calculate the class average (the average of all students’ averages) and print it.
# Print the name of each student, their average grade, and their letter grade.

# Hints:
# Use loops to iterate through the student_grades dictionary.
# You may use sum() and len() functions to help calculate averages.
# Initialize empty dictionaries for student_averages and student_letter_grades before filling them with data.

def create_avarage_grades_dict(student_grades):
    import math
    student_avarages = dict()
    for student, grades in student_grades.items():
        avarage = sum(grades)/len(grades)
        student_avarages[student] = avarage
    return student_avarages

def create_letter_grades_dict(student_avarages):
    student_letter_grades = dict()
    for student, av_grade in student_avarages.items():
        if av_grade < 60:
            student_letter_grades[student] = "F"
        elif 60 <= av_grade < 70:
            student_letter_grades[student] = "D"
        elif 70 <= av_grade < 80:
            student_letter_grades[student] = "C"
        elif 80 <= av_grade < 90:
            student_letter_grades[student] = "B"
        else:
            student_letter_grades[student] = "A"
    return student_letter_grades

def average_of_averages(student_avarages):
    class_av = sum(student_avarages.values())/len(student_avarages)
    return class_av

def print_student_info(student_avarages, student_letter_grades):
    for student in student_avarages.keys():
        print(f"{student}'s avarage grade: {student_avarages[student]}")
        print(f"{student}'s letter grade: {student_letter_grades[student]}")
        print()

def main():
    student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
    }

    student_avarages = create_avarage_grades_dict(student_grades)

    student_letter_grades = create_letter_grades_dict(student_avarages)

    class_av = average_of_averages(student_avarages)
    print(f"class avarage: {class_av}")
    print()

    print_student_info(student_avarages, student_letter_grades)

main()
