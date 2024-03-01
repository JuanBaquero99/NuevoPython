my_range = range(1,5)
for i in my_range: 
    print(i)


other_range = range(0,5,2)
for i in other_range:
    print (i)

another_range = range(0,6,2)
for i in another_range:
    print(i)

print(another_range == other_range)
print (id(another_range))
print(id(other_range)) 
print (another_range is other_range)

#README
#Hay algo importante aquí. Más alla del procedimiento de iteración
#Donde vemos que i esta recorriendo el rango con sus limites y sus saltos
#Es posible que another-range y other_range sean similares porque cumplen un limite similar de distancia entre números y por los saltos
#Sin embargo, al verificar la ubicación de memoría de cada objeto con id
#Podemos determinar que la ubicación en memoría de cada objeto es distinta
#Por lo tanto si comparamos las dos variables con el is, nos indica que es False, son dos objetos distintos
#Alojados en dos lugares de la memoria distinta

