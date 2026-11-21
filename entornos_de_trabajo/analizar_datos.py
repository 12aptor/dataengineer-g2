import pandas as pd

edades = pd.Series([25, 30, 35, 40], index=["Ana", "Luis", "Carlos", "Marta"])
print(edades)

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "Marta"],
    "Edad": [25, 30, 35, 40],
    "Ciudad": ["Lima", "Arequipa", "Cusco", "Lima"]
}

df = pd.DataFrame(datos)
print(df)

""" Leer desde CSV o Excel """
df2 = pd.read_csv("transacciones_paolo_soncco.csv")
# df3 = pd.read_excel("datos.xlsx")
print(df2)

""" Guardar resultados """
df.to_csv("resultado.csv", index=False)

""" Filtrar resultados """
nombres = df[["Nombre", "Ciudad"]]
print(nombres)

mayores_de_30 = df[df["Edad"] > 30]
print(mayores_de_30)

filtro_compuesto = df[(df["Edad"] > 30) & (df["Ciudad"] == "Lima")]
print(filtro_compuesto)

""" Limpieza de datos """
# Contar valores faltantes por columna
df.isnull().sum()

# Eliminar filas con valores nulos
df.dropna()

# Rellenar valores nulos con algún valor especifico (ej. 0)
df.fillna(0)