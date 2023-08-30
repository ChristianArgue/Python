# Determinar si el valor ingresado por el usuario esta dentro del rango 0 - 5

num = int(input('Ingrese un numero dentro del rango (0 - 5): '))

if (num >= 0 and num <= 5):
    print(f'El numero {num} esta dentro del rango')
else:
    print(f'El numero {num} no esta dentro del rango')

# Determinar si la edad pertenece entre ls 20's y los 30's

edad = int(input('Ingrese su edad: '))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

if(veintes or treintas):
    print("Dentro del rango de los 20's o 30's")
else:
    print("No esta dentro de los 20's 0 30's")
