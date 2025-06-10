#lets take sets for in or not in orperators


students = {"sid", "kid", "did"}

student = input("enter the name of a student : ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")