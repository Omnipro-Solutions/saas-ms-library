def suma(a, b):
    """
    Suma dos números

    :param a: Primer número
    :type a: int
    :param b: Segundo número
    :type b: int
    :rtype: int
    :return: Suma de los dos números

    Ejemplo:
    >>> suma(1, 2)
    4

    >>> suma(2, 3)
    5
    """
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero")
    return a / b
