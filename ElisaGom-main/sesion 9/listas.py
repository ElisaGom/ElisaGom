# filtrar listas
id_empleados = [345,45,435,676,345,345,676,764,242]

pares = filter(lambda x: x%2 ==0, id_empleados)

print(list (pares))