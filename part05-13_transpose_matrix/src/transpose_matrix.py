# Write your solution here
def transpose(matrix: list):
  flip_matrix = []
  for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
      new_row.append(matrix[j][i])
    flip_matrix.append(new_row)

  matrix[:] = flip_matrix
  print(matrix)


if __name__ == "__main__":
  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]

  transpose(matrix)

