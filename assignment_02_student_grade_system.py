# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#

score = float(input("Enter your score: "))
if score >= 80:
    print("Grade A!")
elif score >= 70:
    print("Grade B!")
elif score >= 60:
    print("Grade C!")
elif score >= 50:
    print("Grade D!")
else:
    print("Grade F!")   

