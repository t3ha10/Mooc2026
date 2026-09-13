# Write your solution here
def longest(list_str):
  max_number = 0
  longest_str = ""
  for element in list_str:
    if len(element) > max_number:
      max_number = len(element)
      longest_str = element
  return longest_str




if __name__ == "__main__":
  strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
  print(longest(strings))