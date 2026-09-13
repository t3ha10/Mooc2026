# Write your solution here
def everything_reversed(my_list):
  reversed_elements = []
  for i in my_list:
    i = i[::-1]
    reversed_elements.append(i)
  


    result = reversed_elements[::-1]
  return result






if __name__ == "__main__":

  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)