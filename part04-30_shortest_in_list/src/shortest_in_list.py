# Write your solution here
def shortest(mylist):
  shortest_string = mylist[-1]
  for i in range(len(mylist) - 1):
    if len(mylist[i]) < len(shortest_string):
      shortest_string = mylist[i]
  return shortest_string


if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]
  result = shortest(my_list)
  print(result)