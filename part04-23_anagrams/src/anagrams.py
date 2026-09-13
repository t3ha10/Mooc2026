# Write your solution here
def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    hold = list(str2)
    for i in str1:
        character = str(i)
        if character in hold:
            hold.remove(i)
        else:
            return False
 
    return True
 
if __name__ == "__main__":
    print(anagrams("stressed", "desserts"))
