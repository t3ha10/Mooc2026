# Write your solution here
def longest_series_of_neighbours(my_list):
  count = 1
  longest = 0

  for i in range(len(my_list) - 1):
    # print(i, range(len(my_list) - 1))
    if my_list[int(i)] - my_list[int(i) + 1] == 1 or my_list[int(i) + 1] - my_list[int(i)] == 1:
      count += 1
    else:
      if count > longest:
        longest = count
        count = 1
      else:
        count = 1
  if count > longest:
    longest = count
  return longest
    








if __name__ == "__main__":
  # my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
  # print(len(my_list))
  print(longest_series_of_neighbours(my_list))