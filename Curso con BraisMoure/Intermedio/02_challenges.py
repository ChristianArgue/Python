# Challenges

"""

                        EL FAMOSO 'FIZZ BUZZ'
 ____________________________________________________________________
|                                                                    |
| Escribe un programa que muestre por consola (con un print) los     |
| numeros de 1 a 100 (ambos incluidos y con un salto de linea entre  |
| cada impresion), sustituyendo los siguientes:                      |
| - Multiplos de 3 por la palabra 'Fizz'                             |
| - Multiplos de 5 por la palabra 'Buzz'                             |
| - Multiplos de 3 y de 5 a la vez por la palabra 'FizzBuzz'         | 
|____________________________________________________________________|


"""

# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)


# fizzbuzz()

# ---------------------------------------------------------- #

"""

                        ¿ES UN ANAGRAMA?
 ___________________________________________________________________
|                                                                   |
| Escribe una funcion que reciba dos palabras (String) y retorne    |
| verdadero o falso (bool) segun sean o no anagramas.               |
| - Un anagrama consiste en formar uuna palabra reordenando TODAS   |
|   las letras de otra palabra inicial.                             |
| - No hace falta comprobar que ambas palabras existan              |
| - Dos palabras exactamente iguales no son anagramas               |
|___________________________________________________________________|

"""

# def is_anagrama(wordOne, wordTwo):
#     if wordOne.lower() == wordTwo.lower():
#         return False
#     # Usamos sorted para ordenar la palabra en una lista y en orden alfabetico
#     return sorted(wordOne.lower()) == sorted(wordTwo.lower())

# print(is_anagrama('Amor', 'Feo'))

# ----------------------------------------------------------------------- #

"""

                        SUCESION FIBONACCI
 __________________________________________________________________________
|                                                                          |
| Escribe un programa que imprima los 50 primeros numeros de la sucesion   |
| de Fibonacci empezando en 0.                                             |
| - La serie Fibonacci se compone por una sucession de numeros en          |
|   la que el siguiente siempre es la suma de los dos anteriores           |
|   0, 1, 1, 2, 3, 5, 8, 13, ...                                           | 
|__________________________________________________________________________|  

"""

# def fibonacci():
#     prev = 0
#     next = 1
#     for i in range(51):
#         print(prev)
#         fib = prev + next
#         prev = next
#         next = fib

# fibonacci()

# ------------------------------------------------------------------- # 

"""

                            ¿ES UN NUMERO PRIMO?
 ________________________________________________________________________________
|                                                                                |
| Escribe un programa que se encargue de comprobar si un numero es o no primo.   |
| Hecho esto, imprime los numeros primos entre 1 y 100.                          |
|________________________________________________________________________________| 

"""

# def is_prime():
#     for number in range(1, 101):
#         if number >= 2:
#             is_divisible = False
#             for i in range(2, number):
#                 if number % i == 0:
#                     is_divisible = True
            
#             if not is_divisible:
#                 print(number)

# is_prime()        

# -------------------------------------------------------------------- #

"""

                            INVIRTIENDO CADENAS
 _____________________________________________________________________________
|                                                                             |
| Crea un programa que invierta el orden de una cadena de texto               |
| sin usar funciones propias del lenguaje que lo hagan de forma automatica    |
| - Si le pasamos 'Hola Mundo' nos retornaria 'odnuM aloH'                    |
|_____________________________________________________________________________|

"""

def reverse_text(text):
    text_len = len(text)
    reversed_text = ""
    for i in range(0, text_len):
        reversed_text += text[text_len - i - 1]

    return reversed_text

print(reverse_text('Hola Mundo'))