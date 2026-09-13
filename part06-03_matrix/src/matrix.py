# write your solution here
def calculate_matrix():
  with open("matrix.txt") as matrix:
    result = []
    max_value = None
    row_sums = []
    for line in matrix:
      text_numbers = line.split(",")
      sum_line = 0
      for text in text_numbers:
        number = int(text)
        sum_line += number
        if max_value == None or number > max_value:
          max_value = number
      row_sums.append(sum_line)
    return max_value, row_sums
        


def matrix_sum():
  tuple_matrix = calculate_matrix()
  row_sums = tuple_matrix[1]
  sum_rows = 0
  for row_sum in row_sums:
    sum_rows += row_sum
  return sum_rows


def matrix_max():
  tuple_matrix = calculate_matrix()
  return tuple_matrix[0]


def row_sums():
  tuple_matrix = calculate_matrix()
  return tuple_matrix[1]

if __name__ == "__main__":
  # print(calculate_matrix())
  print(matrix_sum())
  print(matrix_max())
  print(row_sums())