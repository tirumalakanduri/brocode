# Student Score Grader (Dict + Function + Conditions + Loop)
# Write a function that takes a dictionary like {'John': 87, 'Alice': 92, 'Bob': 76} and returns a new dictionary with names and their corresponding grades (A, B, C, etc.). 


def student_score(dict):
    grades = {}
    for name, score in dict.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades


student = {'John': 87, 'Alice': 92, 'Bob': 76, 'Daisy': 58}

print(student_score(student))

