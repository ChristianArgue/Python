# Lambdas

suma = lambda first_value, second_value: first_value + second_value
print(suma(5, 3))

multiply = lambda first_value, second_value: first_value * second_value - 3
print(multiply(5, 3))

def sum_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_values(5)(2, 4)) 