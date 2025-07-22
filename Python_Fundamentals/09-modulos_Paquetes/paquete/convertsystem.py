import sys

def dectobin(n):
    binario = ""
    while n > 0:
        b = str(n % 2)
        binario = b + binario
        n //= 2
    return binario


def dectoquin(n):
    quinario = ""
    while n > 0:
        q = str(n % 5)
        quinario =  q + quinario
        n //= 5
    return quinario



def bintodec(n):
    n = str(n)
    decimal = 0
    l = len(n)-1
    for b in n:
        decimal += int(b) * (2**l)
        l -= 1
    return decimal


def quintodec(n):
    n = str(n)
    decimal = 0
    l = len(n) - 1
    for q in n:
        decimal += int(q)*(5 ** l)
        l -= 1
    return decimal


# $ python convertsystem.py dtb 12
# > 1100
if __name__ == "main_":
    if len(sys.argv) == 3:
        if sys.argv[1] == "dtb":
            print(dectobin(int(sys.argv[2])))
        elif sys.argv[1] == "dtq":
            print(dectoquin(int(sys.argv[2])))
        elif sys.argv[1] == "btd":
            print(bintodec(sys.argv[2]))
        elif sys.argv[1] == "qtd":
            print(quintodec(sys.argv[2]))
    else:
        print("Los datos no son correctos.")