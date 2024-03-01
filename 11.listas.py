my_list = [1, 2, 3, 4]
print(my_list)

my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

for e in my_list:
    print(e)

a = my_list
print(a)

print (id(a))
print (id(my_list))

lista_1 = [1,2,3,4]
b = list(lista_1)
print(id(b))
print (id(lista_1))

lista_rango = list(range(100))
double = [i * 2 for i in lista_rango]
print(lista_rango)
print(double)

pares = [i for i in lista_rango if i % 2 == 0] #El operador % nos indica si es par (número divido por dos que da 0)
print(pares)

#README
#1. Reasignar una lista a otra variable no crea otro objeto, sino que siguen ocupando el mismo espacio en memoria
#2. Esa verificación realiza en id lo demuestra, por lo cual es mejor copia esa lista con la función list
#3. Eso evita errores
#4. La comprehension permite sacar valores de una lista, como el ejemplo de los rangos
