# Write your solution here
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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

  copy_sudoku = []
  for i in range(len(sudoku)):
    new_row = []
    for j in range(len(sudoku[i])):
      if i == row_no and j == column_no:
        new_row.append(number)
      else:
        new_row.append(sudoku[i][j])
      # print(f"i: {i}, j: {j}, new_row: {new_row}")
      
    copy_sudoku.append(new_row)
  return copy_sudoku













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

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  # print(grid_copy)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)