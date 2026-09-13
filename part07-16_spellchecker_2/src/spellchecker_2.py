# Write your solution here
from difflib import get_close_matches
if True:
  text = input("Write text: ")
else:
  text = "This is Acually a good and usefull program"

words = text.split(" ")
dictionary = {}
with open("wordlist.txt") as new_file:
  for line in new_file:
    line = line.replace("\n", "")
    dictionary[line] = line

found_wrong_word = []
for word in words:
  lowercase = word.lower()
  if lowercase not in dictionary:
    found_wrong_word.append(word)
    text = text.replace(word, "*" + word + "*")


print(text)
print("suggestions:")
for wrong_word in found_wrong_word:
  text = wrong_word + ": "
  wrong_words = get_close_matches(wrong_word, dictionary)
  for word in wrong_words:
    text = text + word + ", "
  text = text[:-2]
  print(text)
  


    






# if __name__ == "__main__":