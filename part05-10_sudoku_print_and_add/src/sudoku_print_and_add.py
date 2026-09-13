# # Write your solution here
def row_three(sudoku, row_no, col_no):
  for i in range(col_no, col_no + 3):
    element = sudoku[row_no][i]
    if element == 0:
      print("_ ", end="")
    else:
      print(f"{element} ", end="")
  print(" ", end="")
def sudoku_row(sudoku, row_no):
  for i in range(0, len(sudoku[row_no]), 3):
    row_three(sudoku, row_no, i)


def sudoku_three_block(sudoku, position):
  for i in range(position, position + 3):
    sudoku_row(sudoku, i)
    print()

def print_sudoku(sudoku):
  for i in range(0, len(sudoku), 3):
    sudoku_three_block(sudoku, i)
    print()

  
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
  sudoku[row_no][column_no] = number
  return sudoku




if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
  # sudoku  = [
  #   [0, 1, 2, 3, 4, 5, 6, 7, 8],
  #   [9, 10, 11, 12, 13, 14, 15, 16, 17],
  #   [18, 19, 20, 21, 22, 23, 24, 25, 26],
  #   [27, 28, 29, 30, 31, 32, 33, 34, 35],
  #   [36, 37, 38, 39, 40, 41, 42, 43, 44],
  #   [45, 46, 47, 48, 49, 50, 51, 52, 53],
  #   [54, 55, 56, 57, 58, 59, 60, 61, 62],
  #   [63, 64, 65, 66, 67, 68, 69, 70, 71],
  #   [72, 73, 74, 75, 76, 77, 78, 79, 80]
  # ]








  print_sudoku(sudoku)
  add_number(sudoku, 0, 0, 2)
  add_number(sudoku, 1, 2, 7)
  add_number(sudoku, 5, 7, 3)
  print()
  print("Three numbers added:")
  print()
  print_sudoku(sudoku)

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Three numbers added:

# 2 _ _  _ _ _  _ _ _
# _ _ 7  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ 3 _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
