### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("./my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Alberto\nMi apellido es S\n33 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

with open("./my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Flutter")

# os.remove("./my_file.txt")


# .json file


json_file = open("./my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("./my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("./my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("./my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file