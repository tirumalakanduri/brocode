# list comprehension = A consise way to create lists in python
#                     compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]



   # def lc():
    #    doubles = []
    #    for i in range(1, 11):
    #        doubles.append(i*2)
    #    return doubles
    #    

   # print(lc())




doubles = [x * 2 for x in range (1, 11)]
print(doubles)

tirples = [y * 3 for y in range(1, 11)]
print(tirples)
squares = [ z * z for z in range(1, 10)]
print(squares)



fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)



numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)



grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
