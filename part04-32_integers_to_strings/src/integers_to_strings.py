# Write your solution here
def formatted(my_list):
  result = []
  for i in my_list:
    i = f"{i:.2f}"
    result.append(i)
  return result






if __name__ == "__main__":
  my_list = [1.234, 0.3333, 0.11111, 3.446]
  new_list = formatted(my_list)
  print(new_list)
