contador = 0

while contador < 10: #Esto sera infinito porque contador siempre estara en 0
	print (contador)
	contador += 1
	
    #README
    #Podemos ver que se detuvo antes del 10 al momento de ejecutar el programa. 
	
contador_interno = 0
contador_externo = 0

contador_externo = 0
while contador_externo < 5: 
    contador_interno = 0  # Debes inicializar contador_interno en cada iteración del bucle externo
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        if contador_interno <= 3:
            break
        contador_interno += 1  # Incremento de contador_interno dentro del bucle interno
        
    if contador_interno >= 3: 
        break
    
    contador_externo += 1



frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
        print(fruta)

#README
#frutas guarda objetos en una lista. Luego con for va a empezar a recorrer frutas y va almacenar una por una en la variabel fruta
#Guarda una en una
        
estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for elementos in estudiantes:
    print(elementos)

for pais in estudiantes.keys():
    print(pais)

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)

#Readme 
#Esta iterando en el diccionario. Agrega a la variable elementos los objetos que hay en estudiantes
#Agrega a la variable pais los objetos que hay en las llaves {} referente a país
#Suceisvamente






	
	
