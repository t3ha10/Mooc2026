# Write your solution here
def dict_of_numbers():
  basic_number = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
  special_case = {2: "twen",3: "thir", 4: "for", 5: "fif",6: "six", 7: "seven", 8: "eigh", 9: "nine"}
  numbers = {}

  for i in range(0, 100):
    if i == 0:
      numbers[i] = "zero"
    elif i < 10:
      numbers[i] = basic_number[i]
    elif i == 10:
      numbers[i] = "ten"
    elif i == 11:
      numbers[i] = "eleven"
    elif i == 12:
      numbers[i] = "twelve"
    elif i == 14:
      numbers[i] = "fourteen"
    elif i < 20:
      numbers[i] = special_case[i - 10] + "teen"
    else:
      if i % 10 == 0:
        numbers[i] = special_case[i / 10] + "ty" 
      else:
        numbers[i] = special_case[i // 10] + "ty-" + basic_number[i % 10]
  return numbers
    





if __name__ == "__main__":
  numbers = dict_of_numbers()
  print(numbers[2])
  print(numbers[11])
  print(numbers[45])
  print(numbers[99])
  print(numbers[0])


