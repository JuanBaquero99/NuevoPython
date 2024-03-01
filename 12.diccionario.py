my_dict = {
    'Juan': 24,
    'Pablo': 25,
    'Juana': 27,

}

my_dict ['Pedro'] = 20
print(my_dict)

for llaves in my_dict.keys():
    print(llaves)
for valor in my_dict.values():
    print(valor)
for valores in my_dict.items():
    print(valores)

print ('Juan' in my_dict)
print ('Carlos' in my_dict)

#README
#1. Hay maneras de agregar elementos a los dicciones con []
#2. Es posible iterar los diccionarios de acuerdo al valor que queremos: llave, valor o los dos elementos
#3. Es posible verificar con in si un valor se encuentra en dict, lo que nos arroja un booleano