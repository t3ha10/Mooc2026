# Write your solution here
def check_number(string):
  try:
    int(string)
    return True
  except ValueError:
    return False

def check_for_duplicates(list_content):
  filter_list = []

  for i in list_content:
    if i not in filter_list:
      filter_list.append(i)
    else:
      return True
  return False

def check_conditions(list_content):
  numbers = list_content[1:]

  if check_number(list_content[0]) == False or len(numbers) != 7 or check_for_duplicates(numbers):
    return False
  for i in numbers:
    if check_number(i) == False or int(i) < 0 or int(i) > 39:
      return False
  
  return True



def filter_incorrect():
  open("correct_numbers.csv", "w").close()

  with open("lottery_numbers.csv") as new_file:
    for line in new_file:
      parts = line.split(" ")
      contents = parts[1].split(";")

      content = []
      content.append(contents[0])
      winning_lottery_numbers = contents[1].split(",")
      for i in winning_lottery_numbers:
        content.append(i)


      if check_conditions(content):
        with open("correct_numbers.csv", "a") as correct_file:
          correct_file.write(line)


      




if __name__ == "__main__":
  filter_incorrect()
