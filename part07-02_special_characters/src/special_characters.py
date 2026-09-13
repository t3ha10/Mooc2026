# Write your solution here
def separate_characters(my_string: str):
  import string

  ascii_letters_sequence = ""
  punctuation_sequence = ""
  remain_sequence = ""
  for ch in my_string:
    if ch in string.ascii_letters:
      ascii_letters_sequence += ch
    elif ch in string.punctuation:
      punctuation_sequence += ch
    else:
      remain_sequence += ch
  
  return ascii_letters_sequence, punctuation_sequence, remain_sequence



    

if __name__ == "__main__":
  parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
  print(parts[0])
  print(parts[1])
  print(parts[2])