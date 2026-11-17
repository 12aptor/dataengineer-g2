""" Las clases nos permiten implementar el paradigma de Programacion
Orientada a Objetos (POO). Nos permite crear tipos de datos, encapsular
atributos y comportamientos, y organizar código de forma modular y reutilizable. """

class Persona:
    pass

class Vehiculo:
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        # Encapsulación
        self.__codigo = "VW0001"

    def ver_datos(self):
        print(f"Este vehículo es de marca: {self.marca}, color: {self.color}, modelo: {self.modelo} y código: {self.__codigo}")

    # Encapsulación
    def __informacion_privada(self):
        print(f"Esta información es privada: {self.__codigo}")

camioneta = Vehiculo("Toyota", "Blanco", "Hilux")
coche = Vehiculo("VW", "Negro", "Golf")
# print(coche.color)
# coche.ver_datos()
# print(coche.__codigo)
# coche.__informacion_privada()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saltar(self):
        print(f"{self.nombre} ha saltado")

    @staticmethod
    def vacunas(mensaje):
        print(mensaje)

# Herencia: Permite crear clases derivadas que heredan atributos y métodos
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡Miau!")

perro = Animal("Rex")
perro.saltar()
perro.vacunas("Las vacunas están al día")

pelusa = Gato("Pelusa")
pelusa.hablar()
pelusa.saltar()