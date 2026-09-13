# Write your solution here
def invert(dictionary: dict):
  my_obj = {}
  for key, value in dictionary.items():
    my_obj[value] = key
  
  dictionary.clear()
  for key, value in my_obj.items():
    dictionary[key] = value


if __name__ == "__main__":
  s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
  invert(s)
  print(s)
  # {"first": 1, "second": 2, "third": 3, "fourth": 4}