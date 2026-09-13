# Write your solution here
mystring = ""

while mystring != "visual studio code":
    input_string = input("Editor:")
    mystring = input_string.lower()
    if mystring == "word" or mystring == "notepad":
        print("awful")
    elif mystring == "visual studio code":
        print("an excellent choice!")
    else:
        print("not good")