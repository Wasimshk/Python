# Given a dictionary of students and marks, find the student with the highest marks.

data = {"wasim": 7, "azim": 9, "aditya": 19, "obaid": 6, "irshad": 15, "anup": 17, "wajid": 13 }

highest_marks = 0
student = None
for s, score in data.items():
    if highest_marks < score:
        highest_marks = score
        student = s


print(f"the {student} got the highest marks: {highest_marks}")