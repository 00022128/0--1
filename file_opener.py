import json
import csv

file_path1 = "/Users/scorpionn/Desktop/output.txt"
file_path2 = "/Users/scorpionn/Desktop/output.json"
file_path3 = "/Users/scorpionn/Desktop/output.csv"

try:
    with open(file_path1, "r") as file:
        data = file.read()
        print(data)
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content)
    with open(file_path3, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")

