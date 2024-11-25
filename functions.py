#  сложение
def addition(a: int, b: int) -> dict :
    n: int = a + b
    dictionary = {n : n}
    return dictionary

print(addition(1, 2))



# вычитание
def subtraction(a: int, b: int) -> dict :
    n: int = a - b
    dictionary = {n : n}
    return dictionary

print(subtraction(2, 1))



# умножение
def multiplication(a: int, b: int) -> dict :
    n: int = a * b
    dictionary = {n : n}
    return dictionary

print(multiplication(1, 2))