

# ingresar un numero y determinar si es par o impar
numero1 = input("Ingrese un numero: ")
numero1 = int(numero1)

#saber si el par o impar
if (numero1 % 2) == 0:
    print(f"El numero {numero1} es par")


else:
    print(f"El numero {numero1} es impar")

