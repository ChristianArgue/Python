# Tipos de Errores

# ---- SyntaxError -----
# print "Hola Comunidad"   # -Error- ( Descomentar para Error )
print ("Hola Comunidad")

# ---- NameError -----
language = 'Spanish' # -Error- ( Comentar para Error )
print(language)

# ---- IndexError -----
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScrip"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5])  # -Error- ( Descomentar para Error )

# ----- ModuleNotFoundError -----
# import maths  # -Error- ( Descomentar para Error )
import math

# ----- AttributeError -----
# print(math.PI) # -Error- ( Descomentar para Error )
print(math.pi)

# ----- KeyError -----
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
# print(my_dict["Apellid"]) # -Error- ( Descomentar para Error )
print(my_dict["Apellido"])

# ---- TypeError ----
# print(my_list['1']) # -Error- ( Descomentar para Error )
print(my_list[1])

# ---- ImportError ----
# from math import PI # -Error- ( Descomentar para Error )
from math import pi
print(pi)

# ---- ValueError ----
my_int = int("10")
# my_int = int("10 Anios") # -Error- ( Descomentar para Error )
print(my_int)

# ---- ZeroDivisionError ----
# print(4/0) # -Error- ( Descomentar para Error )
print(4/2)