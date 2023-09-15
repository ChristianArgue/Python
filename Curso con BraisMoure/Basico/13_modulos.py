# Modulos

import module

module.sumValues(1, 5, 5)
module.printValue('Hola Python')

from module import sumValues, printValue

sumValues(1, 4, 3)
printValue('Hola Pyhton 2')

import math

printValue(math.pi)
print(math.pow(4, 3))

from math import pi as PI_VALUE

print(PI_VALUE)