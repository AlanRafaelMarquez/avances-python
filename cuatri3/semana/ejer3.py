import random
import copy

SIZE = 9  # Tamaño del Sudoku: 9x9
BOX = 3   # Tamaño de cada subcuadro: 3x3

def print_board(board):
    """Imprime el tablero de forma legible."""
    for i, row in enumerate(board):
        if i % BOX == 0 and i != 0:
            print("-" * (SIZE*2 + BOX - 1))
        line = ""
        for j, val in enumerate(row):
            if j % BOX == 0 and j != 0:
                line += "| "
            line += (str(val) if val != 0 else ".") + " "
        print(line)
    print()

def find_empty(board):
    """Devuelve la primera casilla vacía (fila, col) o None si está completo."""
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, row, col, num):
    """Comprueba si num se puede colocar en (row, col)."""
    # Fila y columna
    if any(board[row][x] == num for x in range(SIZE)): return False
    if any(board[y][col] == num for y in range(SIZE)): return False
    # Subcuadro BOX x BOX
    start_row = (row // BOX) * BOX
    start_col = (col // BOX) * BOX
    for i in range(start_row, start_row + BOX):
        for j in range(start_col, start_col + BOX):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    """Resuelve el Sudoku por backtracking. Retorna True si tiene solución."""
    empty = find_empty(board)
    if not empty:
        return True  # ¡Resuelto!
    r, c = empty
    for n in range(1, SIZE + 1):
        if is_valid(board, r, c, n):
            board[r][c] = n
            if solve(board):
                return True
            board[r][c] = 0
    return False

def fill_grid(board):
    """Genera una solución completa de Sudoku."""
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    nums = list(range(1, SIZE+1))
    random.shuffle(nums)
    for n in nums:
        if is_valid(board, r, c, n):
            board[r][c] = n
            if fill_grid(board):
                return True
            board[r][c] = 0
    return False

def make_puzzle(board, removals=40):
    """
    Elimina 'removals' números de la solución para crear el puzzle.
    No garantiza unicidad de solución, pero funciona bien para principiantes.
    """
    attempts = removals
    while attempts > 0:
        i = random.randrange(0, SIZE)
        j = random.randrange(0, SIZE)
        if board[i][j] != 0:
            backup = board[i][j]
            board[i][j] = 0
            # Opcional: aquí podrías clonar y correr solve() para verificar unicidad
            attempts -= 1
    return board

def generate_sudoku(removals=40):
    """Función principal: devuelve (puzzle, solution)."""
    board = [[0]*SIZE for _ in range(SIZE)]
    fill_grid(board)
    solution = copy.deepcopy(board)
    puzzle = make_puzzle(board, removals)
    return puzzle, solution

if __name__ == "__main__":
    # Genera un Sudoku 'fácil' (40 casillas en blanco)
    puzzle, solution = generate_sudoku(removals=40)
    print("Puzzle:")
    print_board(puzzle)
    print("Solución:")
    print_board(solution)