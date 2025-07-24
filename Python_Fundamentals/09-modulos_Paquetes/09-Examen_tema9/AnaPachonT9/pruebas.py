from anapachont9 import miscelanecadenas, conversiones

print(miscelanecadenas.porcentaje("Hola mundo en Python", 4))
miscelanecadenas.histograma("Esto es una cadena de prueba con muchas vocales")

print("Palabras con 4 vocales diferentes:", miscelanecadenas.cuatrovocales())
print("Texto cifrado:", miscelanecadenas.cesar())
print("Texto descifrado:", miscelanecadenas.descesar())

print("Decimal a Hexadecimal:", conversiones.hexa())
print("Decimal a Octal:", conversiones.octal())
print("Decimal a Romano:", conversiones.romano())
print("Romano a Decimal:", conversiones.romtodec())
