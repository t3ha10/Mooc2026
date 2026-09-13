# Write your solution here
def most_common_character(my_str):
  hold_str = my_str
  most_character = ""
  most_amount = 0
  while len(hold_str) != 0:
    amount_element = hold_str.count(hold_str[int(0)])
    if amount_element > most_amount:
      most_amount = amount_element
      most_character = hold_str[int(0)]



    hold_str = hold_str.replace(hold_str[int(0)], "")
  return most_character

def find_most_common(text):
  counter_list = []
  for character in text:
    
    found = False
    for item in counter_list:
      if item[0] == character:
        item[1] += 1
        found = True
        break
    
    if not found:
      counter_list.append([character, 1])
  
  print('\nHere is the counter_list of each character:')
  print(counter_list)
  print('Now you just need to find most common in counter_list')
  return 0


if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))
  
  second_string = "exemplaryelementary"
  print(most_common_character(second_string))

  # third_string = "exemplaryelementary"
  # print(find_most_common(third_string))