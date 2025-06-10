#3. Count Vowels in a String
#Create a function count_vowels(s) that takes a string and returns the number of vowels in it.
#Example: count_vowels("hello world") should return 3.



def count_vowels(s):
    vowels = ("a", "e","i", "o", "u", "A", "E", "I", "O", "U") #i used tuples because they are immutable.
    count = 0
    for char in s:
        if char in vowels:
            count = count + 1
    return count

print(count_vowels("sudarshan"))  
