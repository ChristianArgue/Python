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
    "language": "Python",
    "website" : "https//chris.dev"
}
