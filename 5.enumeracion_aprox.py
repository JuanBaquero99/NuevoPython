objetivo = int(input('Escoge un numero: '))
epsilon = 0.01 #Que tan cerca queremos llegar de la respuesta
paso = epsilon**2 #Que tanto nos vamos a ir acercando a la respuesta epsilon a la potencia de 2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')

#Readme
#Epsilon es el margen de error. Aceptamos una diferencia de 0,01 
#Ahora, el paso que va ir haciendo es el margen de error de epsilon a la raiz cuadrada. O sea multiplicado por 2
#Va a ir recorriendo un valor absoluto que su respuesta es mayo o igual que epsilon y respuesta menor o igual que objetivo
      