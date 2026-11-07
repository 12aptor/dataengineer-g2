# Determina el mayor de dos números
# numero1 = 10
# numero2 = 20
# Output: El mayor es 20

numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

if numero1 > numero2:
    print("El mayor es ", numero1)
elif numero2 > numero1:
    print("El mayor es ", numero2)
else:
    print("Ambos números son iguales.")