# Write your solution here
def remove_smallest(numbers: list):
  smallest = numbers[0]
  for item in numbers:
    if item < smallest:
      smallest = item
  numbers.remove(smallest)
  # return numbers




if __name__ == "__main__":
  numbers = [2, 4, 6, 1, 3, 5]
  remove_smallest(numbers)
  print(numbers)



# [2, 4, 6, 3, 5]