# Write your solution here
layers = int(input("Layers: "))
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def create_matrix(layers):
  my_matrix = []
  grid_size = layers * 2 - 1
  for i in range(grid_size):
    line = [""] * (grid_size)
    my_matrix.append(line)
  return my_matrix

# def fill_in_row_matrix(my_matrix, layers):
#   for j in range(layers):
#       for i in range(j, layers * 2 - 1 - j):
#         my_matrix[j][i] = characters[layers - 1 - j]
#   return my_matrix

# def fill_in_left_col_matrix(my_matrix, layers):
#   for i in range(0, layers - 1):
#     for j in range(i + 1, layers):
#       if my_matrix[j][i] == "":
#         my_matrix[j][i] = characters[layers - 1 - i]
#   return my_matrix

# def fill_in_right_col_matrix(my_matrix, layers):
#   index_right_col_start = int((len(my_matrix) - 1) / 2 + 1)
#   for i in range(len(my_matrix) - 1, index_right_col_start - 1, -1):
#     for j in range(len(my_matrix) - i, layers):
#       if my_matrix[j][i] == "":
#         my_matrix[j][i] = characters[i - layers + 1]
#   return my_matrix

# def fill_matrix(my_matrix):
#   half_matrix = int((len(my_matrix) - 1) / 2)
#   for i in range(len(my_matrix) - 1, half_matrix, -1):
#     my_matrix[i] = my_matrix[len(my_matrix) - 1 - i]
#   return my_matrix

# def print_out(matrix):
#   for row in matrix:
#     text = ""
#     for col in row:
#       text += col
#     print(text)

# my_matrix = create_matrix(layers)
# matrix_row = fill_in_row_matrix(my_matrix, layers)
# left_col_matrix = fill_in_left_col_matrix(matrix_row, layers)
# half_matrix = fill_in_right_col_matrix(left_col_matrix, layers)
# print_out(fill_matrix(half_matrix))

# For i to layer:
def fill_circle_matrix(matrix, layers):
  grid_size = layers * 2 - 1
  for i in range(layers):
    size_circle = grid_size - i
    for j in range(i, size_circle):
      character = characters[layers - 1 - i]
      # 1. Fill top row
      matrix[i][j] = character
      # 2. Fill bottom row
      matrix[size_circle - 1][j] = character
      # 3. Fill left column
      matrix[j][i] = character
      # 4. Fill right column
      matrix[j][size_circle - 1] = character
  return matrix

def print_out(matrix):
  for row in matrix:
    line = ""
    for col in row:
      line += col
    print(line)
    




create_matrix = create_matrix(layers)
print_out(fill_circle_matrix(create_matrix, layers))

# Layers: 3
# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC

# Layers: 4
# D D D D D D D      i to layer =0v 
# D C C C C C D
# D C B B B C D
# D C B A B C D
# D C B B B C D
# D C C C C C D
# D D D D D D D

