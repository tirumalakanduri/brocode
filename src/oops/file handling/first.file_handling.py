#python file detection.

import os
file_path = r"C:\Users\pavan\OneDrive\Desktop\sid note pad.txt"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isdir(file_path):
        print("that is a dir")
else:
    print("that location doesn't exist ")