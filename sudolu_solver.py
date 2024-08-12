import time
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_sudoku(sudoku):
    print("+---+---+---+---+---+---+")
    for i in range(9):
        row = " | ".join(" ".join(str(num) if num != 0 else '.' for num in sudoku[i][j:j+3]) for j in range(0, 9, 3))
        print(f"| {row} |")
        if (i + 1) % 3 == 0:
            print("+---+---+---+---+---+---+")

def solve(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1,10):

                    # pruebo numeros

                    if valid_number(sudoku,n,i,j):
                        sudoku[i][j] = n
                        if solve(sudoku):
                            return True
                        else:
                            sudoku[i][j] = 0

                # backtracking
                return False
        # ya esta hecho
    return True
    
def valid_number(sudoku,n,i,j):
    row = sudoku[i]
    col = [fila[j] for fila in sudoku]

    # reviso fila
    if n in row:
         return False
    
    # reviso columna
    if n in col: 
        return False
    
    # reviso cuadrado de 3x3
    # box_x = primer fila del cuadrado
    # box_y = primer columna del cuadrado
    box_x = i - i % 3 
    box_y = j - j % 3

    for x in range(box_x, box_x + 3):
        for y in range(box_y, box_y + 3):
            if sudoku[x][y] == n:
                return False

    return True

print("Sudoku inicial:")
print_sudoku(sudoku)

start_time = time.time()  
solve(sudoku)
end_time = time.time() 

print("\nSudoku resuelto:")
print_sudoku(sudoku)

time_taken = end_time - start_time
print(f"\nTiempo: {time_taken} segundos")