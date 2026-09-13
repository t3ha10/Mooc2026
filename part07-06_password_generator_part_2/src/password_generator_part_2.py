# Write your solution here

def generate_strong_password(amount, has_numbers, has_special_characters):
  special_characters = "!?=+-()#"
  import string
  from random import randint, shuffle

  letters = string.ascii_lowercase
  numbers = string.digits
  # characters_pool = letters
  # if has_numbers == True:
  #   characters_pool += numbers

  # if has_special_characters == True:
  #   characters_pool += special_characters
  
  result = ""

  index = list(range(0, amount - 1))
  shuffle(index)

  letter_index = index[0]



  if has_numbers == True:
    number_index = index[1]
    
  if has_special_characters == True:
    special_character_index = index[2]



  for i in range(amount):
    if i == letter_index:
      result += letters[randint(0, len(letters) - 1)]
    elif has_numbers == True and i == number_index:
      result += numbers[randint(0, len(numbers) - 1)]
    elif has_special_characters == True and i == special_character_index:
      result += special_characters[randint(0, len(special_characters) - 1)]
    else:
      random_type = randint(1, 3)
      if random_type == 1 and has_numbers == True:
        random_index_number = randint(0, len(numbers) - 1)
        selected_number = numbers[random_index_number]
        result += selected_number
      elif random_type == 2 and has_special_characters == True:
        random_index_special_character = randint(0, len(special_characters) - 1)
        selected_special_character = special_characters[random_index_special_character]
        result += selected_special_character
      else:
        random_index_letter = randint(0, len(letters) - 1)
        selected_letter = letters[random_index_letter]
        result += selected_letter


  return result



if __name__ == "__main__":
  for i in range(10):
    print(generate_strong_password(5, True, False))
