#python writing files(.txt, .json, .csv)


import json
import csv
employees = [["name", "age", "job"], 
             ["spongebob", 30, "cook"], 
             ["patrick", 37, "unemployee"], 
             ["sandy", 27, "scientist"]]

file_path = "C:/Users/pavan/OneDrive/Desktop/output.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer =  csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

