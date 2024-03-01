#Encontrar raíz cuadrada

objetivo = int(input('Escoge un número'))
respuesta = 0

while respuesta **2 < objetivo:
    print (respuesta)
    respuesta += 1

if respuesta **2 == objetivo:
    print (f'La raiz cuadrada de {objetivo} es {respuesta}')
else: 
    print(f'{objetivo} no tiene una raíz cuadrada exacta')

#Readme
#El usuario ingresa el número que quiere saber la raíz cuadrada
#Mientras que respuesta a la potencia de 2 sea menor que objetivo, se ejecuta
#Entre tanto se va agregando un número al contador de respuesta
#En ese recorridos si la respuesta a la potencia de 2 es igual al objetivo envía mensaje
#Si no puede, detiene e indica que no es exacta
