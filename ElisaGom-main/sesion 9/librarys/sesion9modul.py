import librarys.mixmodulo as mx
archivo = "Power.csv"

carga_datos = mx.cargar_datos(archivo)
print(carga_datos.head())


lst = [1, 2, 3, 4, 5]
prom = mx.calcular_promedio(lst)

print('EL promedio es : ', prom)