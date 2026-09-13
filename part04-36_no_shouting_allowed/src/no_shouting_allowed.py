# Write your solution here
def no_shouting(my_list):
  result = []
  for i in my_list:
    if not str(i).isupper():
      result.append(i)
  return result










if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)
  # ['def', 'lower', 'another lower', 'Capitalized']