# Write your solution here
import string


def change_case(orig_string: str):
  ascii_lowercase_string = string.ascii_lowercase

  result = ""
  for i in range(len(orig_string)):
    if orig_string[i] in ascii_lowercase_string:
      change = orig_string[i].upper()
      result += change
    else:
      change = orig_string[i].lower()
      result += change

  return result



def split_in_half(orig_string: str):
  p1 = orig_string[:len(orig_string) // 2]
  p2 = orig_string[len(orig_string) // 2:]
  return p1, p2




def remove_special_characters(orig_string: str):
  normal_characters = string.ascii_letters + string.digits + " "

  result = ""
  for i in range(len(orig_string)):
    if orig_string[i] in normal_characters:
      result += orig_string[i]
  return result




if __name__ == "__main__":
  my_string = "Well hello there!"
  print(change_case(my_string))

  p1, p2 = split_in_half(my_string)

  print(p1)
  print(p2)

  m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
  print(m2)
