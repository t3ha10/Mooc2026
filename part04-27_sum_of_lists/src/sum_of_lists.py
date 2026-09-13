# Write your solution here
def list_sum(list1, list2):
  if len(list1) != len(list2):
    return
  sum_lists = []
  for i in range(len(list1)):
    sum_lists.append(list1[i] + list2[i])
  return sum_lists


if __name__ == "__main__":
  a = [1, 2, 3]
  b = [7, 8, 9]
  print(list_sum(a, b))