# Write your solution here
def no_vowels(my_str):
  result = ""
  vowels_array = ["i","a","e","o", "u"]
  for i in my_str:
    if not str(i) in vowels_array:
      result += str(i)
  return result



if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))