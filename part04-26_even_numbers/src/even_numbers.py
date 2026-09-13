# Write your solution here
def even_numbers(my_list):
  list_result = []
  for i in my_list:
    if int(i) % 2 == 0:
      list_result.append(int(i))
  return list_result

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  new_list = even_numbers(my_list)
  print("original", my_list)
  print("new", new_list)