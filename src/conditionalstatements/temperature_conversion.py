unit = input("is this temperature in celsius or farenheitb(c/f)")
temp = float(input("enter the temperature : "))

if unit == "c" or unit == "C":
    temp = round((9 * temp) / 5 +32, 1)
    print(f" the temperature in fahrenheit is { temp }f")
elif unit == "F" or unit == "f":
    temp = round((temp -32) * 5 /9, 1)
    print(f"the temperature in celsius is : { temp}")
else:
    print(f"{unit} is an invalid unit of measurement")