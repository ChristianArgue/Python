# Operadores Aritmeticos
operandoA = 3
operandoB = 2

suma = operandoA + operandoB
# print('La suma es:', suma)
print(f'La suma es: {suma}')

resta = operandoA - operandoB
print(f'La resta es: {resta}')

multiplicaion = operandoA * operandoB
print(f'La multiplicaion es: {multiplicaion}')

division = operandoA / operandoB
print(f'La division es: {division}')

division = operandoA // operandoB
print(f'La division tipo(int) es: {division}')

modulo = operandoA % operandoB
print(f'El residuo es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado es: {exponente}')

# Operador de Asignacion
miVaribale = 10
print(miVaribale)

# Operador de Reasignacion
miVaribale = miVaribale + 1
miVaribale += 1
print(miVaribale)

#Operador de Comparacion
a = 4
b = 5
resultado = (a == b)
print(f'Resultado == : {resultado}')

resultado = (a != b)
print(f'Resultado != : {resultado}')

resultado = (a > b)
print(f'Resultado > : {resultado}')

resultado = (a >= b)
print(f'Resultado >= : {resultado}')

resultado = (a < b)
print(f'Resultado < : {resultado}')

resultado = (a <= b)
print(f'Resultado <= : {resultado}')

# Operadores Logicos
a = True
b = False

resultado = (a and b)
print(resultado)

resultado = (a or b)
print(resultado)

resultado = not b
print(resultado)