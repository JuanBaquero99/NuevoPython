def factorial (n) :

    """""Calcula el factorial de n

    n int > 0
    return n
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un número: '))
resultado = factorial(n)
print (resultado)

#README
#1. Se define el factorial el cual recibe el parametro n
#2. Para no comprometer el ciclo, si es 1, devuelve el valor a n
#3. Si es otro número devuele n multiplicado por factorial que es n - 1
#4. Es decir n(4) * 3(4-1) y se retorna a la n de la función
#5. Luego retornado queda en 3 y se repite el proceso. 3*2. 2*1