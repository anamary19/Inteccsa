# Trabajando con cadenas (strings) e iterando en ellas con bucles (loops)

# Recorrer Cadenas
# while
curso = "Python Fundamentals"
i = 0
longitud = len(curso)

while i < longitud:
    print(curso[i])
    i += 1
    
# for
for c in curso: #manera mas sencilla de recorrer una cadena usando for
    print(c)
    

#usando range en el bucle for también es posible recorrerlo ya que la variable i  toma el valor de cada iteración en el string 
longitud = len(curso)
for i in range(longitud):
    print(curso[i])
    
