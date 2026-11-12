""" Definición de funciones """
def saludar():
    print("¡Hola!")

""" Llamada a la función """
saludar()

""" Función con parámetros """
def sumar(a, b):
    c = a + b
    return c

resultado = sumar(3, 5)
print(resultado)

""" Función con parámetros y valor por defecto """
def saludar_persona(nombre="Invitado"):
    print(f"Hola, {nombre}")

saludar_persona()

""" Funciones con número variable de argumentos """
""" *args """
def mostrar_numeros(*args):
    # args: (1, 2, 3)
    for numero in args:
        print(numero)

mostrar_numeros(1, 2, 3)

""" **kwargs """
def mostrar_informacion(**kwargs):
    # kwargs: {'nombre': 'Eduardo', 'edad': 30}
    for clave in kwargs:
        print(clave, kwargs[clave])

mostrar_informacion(nombre="Eduardo", edad=30)