# Write your solution here
def generate_password(number):
  import string
  from random import randint

  characters = string.ascii_lowercase
  result = ""
  for i in range(number):
    random_number = randint(0, len(characters) - 1)
    selected = characters[random_number]
    result += selected
  return result






if __name__ == "__main__":
  for i in range(10):
    print(generate_password(8))