objetivo = int(input('Escoge un numero: '))
epsilon = 0.001 #El margen de diferencia con la raiz cuadrada
bajo = 0.0
alto = max(1.0, objetivo) 
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')

#Readme
#1. El max es la función que define un inicio y un tope de busqueda. Es decir, dado por el número que ingresa
#2. Ahora, para ir reduciendo el margen de busqueda, la respuesta que va obteniendo(ver print en consola) la va diviendo en 2
#3. Es decir, si el objetivo es 9, primero saca la mitad de nueve siendo 4.5. 
#4. Ahora el margen de busqueda es de 0,0 a 4,5. sacando la mitad, siendo 2,25. Así sucesivamente
#5. con el while va a recorrer respuesta en valor absoluto (no negativo)
#6. Se resta, toda vez que es necesario encontrar la diferencia que hay entre respuesta**2 y objetivo
#7 ese dato de diferencia debe ser comparado con epsilon indicando si es mayor o igual a este
#Es decir al restarlos se obtiene que tan lejos esta respuesta de objetivo 
#8 De este modo a medida que el ciclo avanza y va restando, es comparado con el epsilon para ver que tan cerca esta del valor
#9 Si esta diferencia es menor que epsilon, se considera que la aproximación es lo suficientemente buena y el bucle while termina. Si es mayor o igual a epsilon, el bucle continúa ejecutándose, lo que implica que la aproximación aún no es lo suficientemente precisa y se necesitan más iteraciones del algoritmo para refinarla.
#10 con el if si respuesta es menor que el objetivo bajo es el retorno de respuesta. 
#11 es decir que este bajo de nuevo se sumara con el alto y se dividira por dos, para reducir el margen
