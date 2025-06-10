# in AND  both the both the conditions must be true.

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("it is hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("its is sunny")
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
    print ("it is sunny")


