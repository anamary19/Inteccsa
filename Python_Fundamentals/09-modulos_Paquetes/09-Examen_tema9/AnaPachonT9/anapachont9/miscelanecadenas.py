# miscelanecadenas.py

def porcentaje(frase, cc=4):
    palabras = frase.split()
    menos = sum(1 for palabra in palabras if len(palabra) <= cc)
    mas = len(palabras) - menos
    total = len(palabras)

    if total == 0:
        return (0.0, 0.0)

    porcentaje_menos = (menos / total) * 100
    porcentaje_mas = (mas / total) * 100
    return (porcentaje_menos, porcentaje_mas)


def histograma(frase):
    frase = frase.lower()
    vocales = 'aeiou'
    contador = {v: 0 for v in vocales}

    for letra in frase:
        if letra in contador:
            contador[letra] += 1

    ordenado = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    for vocal, frecuencia in ordenado:
        if frecuencia > 0:
            print(f"{vocal} {frecuencia} {'*' * frecuencia}")


def cuatrovocales():
    texto = input("Introduce el texto: ")
    palabras = texto.split()
    contador = 0

    for palabra in palabras:
        vocales_encontradas = set()
        for letra in palabra.lower():
            if letra in 'aeiou':
                vocales_encontradas.add(letra)
        if len(vocales_encontradas) >= 4:
            contador += 1

    return contador


def cesar():
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz,.-¿?='
    texto = input("Introduce el texto a cifrar: ")
    cifrado = ''
    for letra in texto:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) + 6) % len(alfabeto)
            cifrado += alfabeto[indice]
        else:
            cifrado += letra
    return cifrado


def descesar():
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz,.-¿?='
    texto = input("Introduce el texto cifrado: ")
    descifrado = ''
    for letra in texto:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) - 6) % len(alfabeto)
            descifrado += alfabeto[indice]
        else:
            descifrado += letra
    return descifrado
