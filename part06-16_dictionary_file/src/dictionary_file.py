# Write your solution here
while True:
  print("1 - Add word, 2 - Search, 3 - Quit")
  function = int(input("Function: "))
  if function == 3:
    print("Bye!")
    # open("dictionary.txt", "w").close()
    break
  elif function == 1:
    finnish = input("The word in Finnish: ")
    english = input("The word in English: ")
    with open("dictionary.txt", "a") as dictionary_file:
      dictionary_file.write(f"{finnish};{english}\n")
      print("Dictionary entry added")
  else:
    dictionary = {}
    with open("dictionary.txt") as dictionary_file:
      for line in dictionary_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        dictionary[parts[0]] = parts[1]


    search_item = input("Search term: ")
    found_words = {}
    for finnish, english in dictionary.items():
      if finnish.find(search_item) != -1 or english.find(search_item) != -1:
      # if search_item in finnish or search_item in english:
        found_words[finnish] = english


    for finnish, english in found_words.items():
      print(f"{finnish} - {english}")






