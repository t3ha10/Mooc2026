# Write your solution here
def create_tuple(x: int, y: int, z: int):
  first_index_tuple = min(x, y, z)
  second_index_tuple = max(x, y, z)
  third_index_tuple = x + y + z
  my_tuple = (first_index_tuple, second_index_tuple, third_index_tuple)
  return my_tuple





if __name__ == "__main__":
  print(create_tuple(5, 3, -1))