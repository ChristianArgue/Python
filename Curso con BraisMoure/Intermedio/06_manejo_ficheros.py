# Manejo de Ficheros
import os

# ---- .txt file ----
txt_file = open("Curso con BraisMoure/Intermedio/my_file.txt", "w+")
txt_file.write("Mi Nombre es Christian\nMi Apellido es Arguello\nMi edad es 26\nY mi lenguaje preferido es Python")
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

with open("Curso con BraisMoure/Intermedio/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Curso con BraisMoure/Intermedio/my_file.txt")

# ---- .json file ----
import json

json_file = open("Curso con BraisMoure/Intermedio/my_file.json", "w+")

json_test = {
    "name"    : "Christian",
    "surname" : "Arguello",
    "age"     : 26,
    "language": ["Python", "Swift", "Kotlin"],
    "website" : "https//chris.dev"
}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Curso con BraisMoure/Intermedio/my_file.json") as my_json:
    for line in my_json.readlines():
        print(line)

json_dict = json.load(open("Curso con BraisMoure/Intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# ---- .csv file ----
import csv

csv_file = open("Curso con BraisMoure/Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Christian", "Arguello", 26, "Python", "https://chris.dev"])
csv_writer.writerow(["Roswell", "", 2, "Cobol", ""])

csv_file.close()


# ---- .xlsx file ----
# import xlrd        # Debe instalrse el modulo


# ---- .xml file ----
import xml