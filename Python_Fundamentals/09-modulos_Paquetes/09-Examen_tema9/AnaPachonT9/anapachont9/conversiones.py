# conversiones.py

def hexa():
    try:
        num = int(input("Introduce un número decimal: "))
        return hex(num)[2:].upper()
    except ValueError:
        return "Entrada no válida. Debes introducir un número entero."


def octal():
    try:
        num = int(input("Introduce un número decimal: "))
        return oct(num)[2:]
    except ValueError:
        return "Entrada no válida. Debes introducir un número entero."


def romano():
    try:
        num = int(input("Introduce un número decimal: "))
        if not (0 < num < 4000):
            return "Debe estar entre 1 y 3999"

        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        resultado = ''
        for val, simb in valores:
            while num >= val:
                resultado += simb
                num -= val
        return resultado
    except ValueError:
        return "Entrada no válida. Debes introducir un número entero."


def romtodec():
    rom = input("Introduce un número romano (mayúsculas): ").upper()
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for letra in reversed(rom):
        if letra not in valores:
            return "Número romano no válido"
        valor = valores[letra]
        if valor < prev:
            total -= valor
        else:
            total += valor
            prev = valor
    return total
