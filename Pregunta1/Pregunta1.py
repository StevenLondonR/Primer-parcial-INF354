
with open('Raisin_DatasetComas.csv', 'r', encoding='utf-8') as file:
    # Lee todas las líneas del archivo
    lines = file.readlines()

    # Inicializa un diccionario vacío para almacenar los datos de cada columna
    columnas = {}

    # Itera sobre cada línea del archivo
    for line in lines:
        # Elimina cualquier espacio en blanco adicional y divide la línea en columnas
        columns = line.strip().split(';')
        
        # Itera sobre cada columna en la línea
        for i, column in enumerate(columns):
            # Si es la primera columna, agrega una lista vacía para esa columna en el diccionario
            if i not in columnas:
                columnas[i] = []
            
            # Agrega el valor de la columna a la lista correspondiente
            columnas[i].append(column)

# Calcula el cuartil para cada columna
for columna, valores in columnas.items():
    valores_ordenados = valores
    cuartil = valores_ordenados[int(len(valores_ordenados) * 0.3)]  # Calcula el percentil 90
    print(f"Quartil de la columna {columna + 1}: {cuartil}")

# Calcula el percentil para cada columna
for columna, valores in columnas.items():
    valores_ordenados = valores
    percentil8 = valores_ordenados[int(len(valores_ordenados) * 0.8)]  # Calcula el percentil 90
    print(f"Percentil 80 de la columna {columna + 1}: {percentil8}")


