# Write your solution here
def read_words_file():
  with open("words.txt") as dictionary_file:
    words_list = {}
    for line in dictionary_file:
      line = line.replace("\n", "")
      words_list[line] = line
    return words_list
def words(n: int, beginning: str):
  from random import shuffle
  found_words = []
  words_list = read_words_file()
  for i in words_list:
    if i.find(beginning) == 0:
      found_words.append(i)


  shuffle(found_words)
  if len(found_words) < n:
    raise ValueError

  n_words = []
  i = 0
  while True:
    if len(n_words) == n:
      break


    if found_words[i] not in n_words:
      n_words.append(found_words[i])

    if i == len(found_words) - 1 and len(n_words) != n:
      raise ValueError
      break

    i += 1

  return n_words



if __name__ == "__main__":
  word_list = words(500, "car")
  for word in word_list:
    print(word)