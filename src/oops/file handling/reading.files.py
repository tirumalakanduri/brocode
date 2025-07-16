#PYTHON reading files(.txt, .json, .csv)
 
import _json

file_path = "C:/Users/pavan/OneDrive/Desktop/output.json"

try:
    with open(file_path, "r" ) as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")