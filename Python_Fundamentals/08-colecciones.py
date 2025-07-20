# [elemento0,elemento1,elemento3,...]

lista1 = [1,2,3,4,5,6]
lista2 = ["a","b","c","d","e"]

print(lista1)
print(lista2)

# Indexación de los elementos de una lista 
lista = ["a","b","c","d","e"]

e1 = lista[-5]
e2 = lista[-4]
e5 = lista[-1]
print(e2)

# Iterando listas
lista = [1,2,3,4,5,6]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1
    
for i,e in enumerate(lista):
    print(i,e)
    
    
# Sublistas
lista = ["a","b","c","d","e"]
sublista1 = lista[1:3] #Indices positivos
sublista2 = lista[-4:-1] #Indices negativos
print(sublista1)
print(sublista2)