# Ejercicio

## Contexto

El área comercial tiene un archivo facturacion.csv con los montos facturados y el estado de cuenta
de cada cliente, pero no tiene sus datos de contacto ni ubicación. Por otro lado, el sistema central expone los datos maestros de los usuarios a través de una API REST.

## Objetivo
Contruir un pipeline en Python aplicando POO para cruzar ambas fuentes de datos, limpiar inconsistencias y generar un reporte ejecutivo en consola usando ´rich´

1. Generar una lista de datos en un documento .csv ejecutando ´python generar_datos.py´
2. Recuperar una lista de 10 usuarios de [jsonplaceholder]('https://jsonplaceholder.typicode.com/')
3. Limpiar los datos
4. Asociar estos datos con los registros del documento .csv
5. Generar un reporte ejecutivo en consola