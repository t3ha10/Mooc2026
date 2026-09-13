# Write your solution here
list = []
word = ''
while True:
  word = input("Word: ")
  if word in list:
    break
  list.append(word)
print("You typed in", len(list), "different words")
