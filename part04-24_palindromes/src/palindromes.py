# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(myStr):
  if myStr[-1] != myStr[0]:
    return False
  

  number = int(len(myStr) / 2)
  str1 = myStr[:number]
  str2 = myStr[-1:-number - 1:-1]

  if str1 == str2:
    return True
  else:
    return False





result = False
while result == False:
    myStr = input("Please type in a palindrome:")
    if palindromes(myStr) == True:
      print(myStr, "is a palindrome!")
      result = True
    else:
      print("that wasn't a palindrome")
