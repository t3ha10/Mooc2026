# Write your solution here
def distinct_numbers(my_list):
  result = []
  for i in my_list:
    if int(i) not in result:
      result.append(int(i))

  result.sort()
  return result

if __name__ == "__main__":
  my_list = [3, 2, 2, 1, 3, 3, 1]
  print(distinct_numbers(my_list)) # [1, 2, 3]