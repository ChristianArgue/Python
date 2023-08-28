# - En el siguiente ejercicio se solicita calcular el area y el perimetro de un rectangulo,
# para ello deberemos crear las siguientes variables:

# alto (int)
# ancho (int)

# - El ususario debe proporcionar los valores de largo y ancho,
# y despues se debe imprimir el resultado en el siguiente formato
# (no usar acentos y respetar los espacios, mayusculas, minusculas y saltos de linea):

# Proporciona el alto:
# Proporciona el ancho:
# Area: <area>
# Perimetro: <perimetro>

# Las formulas para calcular el area y el perimetro de un rectangulo son:
# Area: alto * ancho
# Perimetro: (alto + ancho) * 2

alto = int(input('Proporcione el alto: '))
ancho = int(input('Proporcione el ancho: '))

Area = alto * ancho
Perimetro = (alto + ancho) * 2

print(f'Area: {Area}')
print(f'Perimetro: {Perimetro}')