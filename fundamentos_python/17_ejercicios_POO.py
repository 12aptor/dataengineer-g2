""" Recuperar la información de datos.csv y construir una lista de
diccionario con estos datos, ademas se debe ordenar por orden alfabetico
en base a los apellidos, tambien se les debe generar una contraseña
encriptada por defecto en base a la fecha de nacimiento """
# Output [{"id": 1, "nombre": "...", ..., "activo": true}, {}, ..., {}]

import csv

class Usuario:
    def __init__(
        self,
        id,
        nombre,
        apellido,
        email,
        telefono,
        ciudad,
        pais,
        fecha_registro,
        activo
    ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_registro = fecha_registro
        self.activo = activo

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "ciudad": self.ciudad,
            "pais": self.pais,
            "fecha_registro": self.fecha_registro,
            "activo": self.activo
        }

def main():
    usuarios_objetos = []

    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        n_fila = 0
        for fila in lector:
            n_fila = n_fila + 1
            if n_fila == 1:
                continue

            usuario = Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6],
                fila[7],
                fila[8]
            )
            usuarios_objetos.append(usuario)

    def obtener_apellido(usuario):
        return usuario.apellido.lower()

    usuarios_ordenados = sorted(
        usuarios_objetos,
        key=obtener_apellido
    )

    resultado_final = []
    for user in usuarios_ordenados:
        resultado_final.append(user.to_dict())

    print(resultado_final)

if __name__ == "__main__":
    main()