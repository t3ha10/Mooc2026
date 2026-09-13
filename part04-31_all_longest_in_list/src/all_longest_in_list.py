# Write your solution here

def length_of_longest(my_list):
  longest = 0
  for i in my_list:
    if len(i) > longest:
      longest = len(i)
  return longest


def all_the_longest(my_list):
  len_longest = length_of_longest(my_list)
  result = []
  for i in my_list:
    if len(i) == len_longest:
      result.append(i)
  return result






if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

  result = all_the_longest(my_list)
  print(result) # ['dorothy', 'richard']