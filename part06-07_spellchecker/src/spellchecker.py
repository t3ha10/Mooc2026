# write your solution here
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

for word in words:
  lowercase = word.lower()
  if lowercase not in dictionary:
    text = text.replace(word, "*" + word + "*")
  
print(text)

    




