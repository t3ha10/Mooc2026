# write your solution here
def largest():
  with open("numbers.txt") as new_file:
    largest_number = None
    for line in new_file:
      number = int(line)
      if largest_number == None or number > largest_number:
        largest_number = number
    return largest_number

if __name__ == "__main__":
  print(largest())


