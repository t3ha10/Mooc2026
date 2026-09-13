# Write your solution here
# def count_letter(my_str):
#   letter_counter = {}
#   for i in my_str:
#     if i not in letter_counter:
#       letter_counter[i] = 0
#     letter_counter[i] += 1
#   return letter_counter
# def histogram(my_str):
#   letter_counter = count_letter(my_str)


#   for key, value in letter_counter.items():
#     print(f"{key} {value * '*'}")

def histogram(my_str):
  letter_counter = {}
  for i in my_str:
    if i not in letter_counter:
      letter_counter[i] = ""
    letter_counter[i] += "*"

  
  for key, value in letter_counter.items():
    print(f"{key} {value}")










if __name__ == "__main__":

  histogram("statistically")
  histogram("abba")