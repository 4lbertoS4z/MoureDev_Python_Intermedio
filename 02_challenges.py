### Challenges ###

# fizz_buzz
# Write a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
# If the number is a multiple of 3 the output should be "Fizz".

# If the number given is a multiple of 5, the output should be "Buzz".

# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".

# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.


def fizzbuzz():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
print("FizzBuzz")
fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

print("Anagrama")
def is_anagram(word1,word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("Roma","Amor"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

print("Fibonacci")

def fibonacci():
    prev = 0
    next = 1

    for i in range(50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
print("¿Primo?")
def is_prime():
    for number in range(1,101):
        if number >= 2:
            is_divisible = False

            for index in range(2,number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

is_prime()                    

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

print("Invertir cadena")

def reverse_string(string):
    reversed = ""
    for letter in string:
        reversed = letter + reversed
    return reversed

print(reverse_string("Hola mundo"))