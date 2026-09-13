# Write your solution here
def same_chars(mystr, index1, index2):
    if  index1 >= len(mystr) or index2 >= len(mystr):
        return False
    elif mystr[index1] == mystr[index2]:
        return True
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))