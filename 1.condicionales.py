num_1 = int(input('Escoge un número:')) #int convierte el input en entero
num_2 = int(input('Escoge otro número'))

if num_1 < num_2: #condicional
    print (f'Numero {num_1} es menor que {num_2}') #formato para asociar la variable a un string
elif num_1 > num_2:
    print (f'Número {num_1} es mayor que {num_2}') #Formato para asociar la variable a un string
else: 
    print ("Los dos número son iguales")

name = input('Como te llamas: ')
edad = int(input('Cual es tu edad: '))

if edad < 18:
    print(f'{name} Es menor de edad')
elif edad >= 18:
    print(f'{name} Es mayor de edad')

#Readme
    #El anterior programa define una variable, su objeto es el string que la persona ingrese (input)
    #El objeto de edad, se transofmra en int ya que input automatico recibe strings
    #if es la condicional, si la el objeto de la variable es menor que 18
    #Imprime en pantalla, la f le da el formato donde lo que esta dentro de las llaves {objeto nombre} se concatena con "Es menor de edad"
    #elif, pero si no se cumple la condición anterior y una sintaxis formateada igual que la anterior
