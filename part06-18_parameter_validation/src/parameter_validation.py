# Write your solution here
def new_person(name: str, age: int):
  length = len(name)
  if length == 0 or length > 40 or name.find(" ") == -1 or age < 0 or age > 150:
    raise ValueError

  return name, age



if __name__ == "__main__":
  print(new_person("had", -2))
