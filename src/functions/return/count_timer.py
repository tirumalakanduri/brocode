import time

def count(end,start = 0):
    for x in range(start, end + 1):
        print(f"00:00:0{x}")
        time.sleep(1)
    print("done!")

count(10)