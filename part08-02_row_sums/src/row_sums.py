# Write your solution here

def row_sums(my_matrix: list):
  for i in my_matrix:
    sum_row = sum(i)
    i.append(sum_row)
    


if __name__ == "__main__":
  my_matrix = [[1, 2], [3, 4]]
  row_sums(my_matrix)
  print(my_matrix)