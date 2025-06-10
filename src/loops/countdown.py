import time

my_time = int(input("enter the time in seconds: "))

for i in range(my_time, 0, -1):
    seconds = i % 60                  #here 60milli seconds in a second
    minutes = int(i/60) % 60          # here %60  is written because we have 60 seconds in a minute
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times up!")

