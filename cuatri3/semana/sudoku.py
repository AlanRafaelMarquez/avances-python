import copy


TAMAÑO = 9              
TAMAÑO_CUADRANTE = 3     
def imprimir_tablero(matriz):
    for fila_indice, fila in enumerate(matriz):
        if fila_indice % TAMAÑO_CUADRANTE == 0 and fila_indice != 0:
            print("-" * (TAMAÑO * 2 + TAMAÑO_CUADRANTE - 1))
        linea = ""
        for col_indice, valor in enumerate(fila):
            if col_indice % TAMAÑO_CUADRANTE == 0 and col_indice != 0:
                linea += "| "
            linea += (str(valor) if valor != 0 else ".") + " "
        print(linea)
    print()
def encontrar_casilla_vacia(matriz):
    for fila in range(TAMAÑO):
        for columna in range(TAMAÑO):
            if matriz[fila][columna] == 0:
                return fila, columna
    return None
def es_movimiento_valido(matriz, fila, columna, numero):
    for c in range(TAMAÑO):
        if matriz[fila][c] == numero:
            return False
    for f in range(TAMAÑO):
        if matriz[f][columna] == numero:
            return False
    inicio_fila = (fila // TAMAÑO_CUADRANTE) * TAMAÑO_CUADRANTE
    inicio_col = (columna // TAMAÑO_CUADRANTE) * TAMAÑO_CUADRANTE
    for f in range(inicio_fila, inicio_fila + TAMAÑO_CUADRANTE):
        for c in range(inicio_col, inicio_col + TAMAÑO_CUADRANTE):
            if matriz[f][c] == numero:
                return False
    return True
def resolver_sudoku(matriz):
    casilla = encontrar_casilla_vacia(matriz)
    if not casilla:
        return True  
    fila, columna = casilla
    for numero in range(1, TAMAÑO + 1):
        if es_movimiento_valido(matriz, fila, columna, numero):
            matriz[fila][columna] = numero
            if resolver_sudoku(matriz):
                return True
            matriz[fila][columna] = 0
    return False
def llenar_tablero(matriz):
    casilla = encontrar_casilla_vacia(matriz)
    if not casilla:
        return True
    fila, columna = casilla
    for numero in range(1, TAMAÑO + 1):
        if es_movimiento_valido(matriz, fila, columna, numero):
            matriz[fila][columna] = numero
            if llenar_tablero(matriz):
                return True
            matriz[fila][columna] = 0
    return False
def quitar_casillas(matriz, cuantas):
    hechas = 0
    for fila in range(TAMAÑO):
        for columna in range(TAMAÑO):
            if hechas >= cuantas:
                return
            if matriz[fila][columna] != 0:
                matriz[fila][columna] = 0
                hechas += 1
def generar_sudoku_basico(cuadros_a_quitar=40):
    matriz = [[0] * TAMAÑO for _ in range(TAMAÑO)]
    llenar_tablero(matriz)
    solucion = copy.deepcopy(matriz)
    quitar_casillas(matriz, cuadros_a_quitar)
    puzzle = matriz
    return puzzle, solucion
if __name__ == "__main__":
    puzzle, solucion = generar_sudoku_basico(cuadros_a_quitar=40)
    print("Puzzle:")
    imprimir_tablero(puzzle)
    print("Solución:")
    imprimir_tablero(solucion)