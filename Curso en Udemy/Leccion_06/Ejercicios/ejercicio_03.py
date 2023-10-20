"""
Calculadora De Impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

def calcularImpuesto(total, iva):
    return total + total * (iva/100)

pago_sin_impuesto = int(input('Ingrese el pago sin impuesto: '))
monto_de_impuesto = int(input('Ingrese el monto del impuesto: '))
valor_total = calcularImpuesto(total=pago_sin_impuesto, iva=monto_de_impuesto)

print(f'Pago con impuesto: {valor_total}')