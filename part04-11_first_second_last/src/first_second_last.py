# Write your solution here
def first_word(mystr):
    end_position = mystr.find(" ")
    return mystr[0:end_position]

def second_word(mystr):
    start_position = len(first_word(mystr)) + 1
    new_str = mystr[start_position:]
    if new_str.find(" ") == -1:
        return new_str
    return first_word(new_str)

def last_word(mystr):
    i = 0
    while i > -len(mystr):
        i -= 1
        if mystr[i] == " ":
            return mystr[i + 1:]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))