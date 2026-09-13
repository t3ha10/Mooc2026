# Write your solution here

def read_input(str_input, min_bound, max_bound):
  while True:
    try:
      user_input = input(str_input)
      number = int(user_input)
      if number > min_bound and number < max_bound:
        return number
    except:
      pass
    print(f"You must type in an integer between {min_bound} and {max_bound}")


if __name__ == "__main__":
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)
