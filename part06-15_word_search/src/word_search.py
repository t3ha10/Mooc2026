# Write your solution here
def read_words_file(filename):
  word_list = []
  with open(filename) as list_file:
    for line in list_file:
      line = line.replace("\n", "")
      word_list.append(line)
    return word_list


def find_words(search_term: str):
  word_list = read_words_file("words.txt")
  found_words = []

  if "." in search_term:
    word_length = len(search_term)
    for word in word_list:
      if word_length == len(word):
        for i in range(word_length):
          if search_term[i] != word[i] and search_term[i] != ".":
            # print(i, search_term[i], word[i], word, search_term[i] != word[i], search_term[i] != ".")
            break
        else:
          found_words.append(word)
        
        
  elif "*" in search_term:
    if search_term[0] == "*":
      for word in word_list:
        if word.endswith(search_term[1:]):
          found_words.append(word)


    else:
      for word in word_list:
        if word.startswith(search_term[:-1]):
          found_words.append(word)

  
  else:
    for word in word_list:
      if search_term == word:
        found_words.append(word)

  return found_words


if __name__ == "__main__":
  print(find_words("*vokes"))