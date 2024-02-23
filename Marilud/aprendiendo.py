# Matriz bidimensional 3*3.

matriz = [
    [1, 2, 3],
    [2, 8, 1],
    [3, 9, 4]
]

# Valor que se busca
valor_buscado = 4

# Variables en que se busca
fila_buscada = 0
columna_busca = 0

#
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_buscada = fila
            columna_hallada = columna

            break  # Detener la búsqueda al encontrar el número
    if fila_buscada != 0:

        break  # Salir al encontrar el valor.

# Revisar si se encontró y la posición del número encontrado
if fila_buscada != 0:
    print(f"Encontrado el {valor_buscado} en la fila {fila_buscada} y columna {columna_hallada}")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
