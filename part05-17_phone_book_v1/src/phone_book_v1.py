# Write your solution here
list_phone_numbers = {}
while True:
  command = int(input("command (1 search, 2 add, 3 quit): "))
  if command == 3:
    print("quitting...")
    break
  
  name = input("name: ")
  
  if command == 2:
    number = input("number: ")

    list_phone_numbers[name] = number

    print("ok!")
  
  if command == 1:
    if name in list_phone_numbers:
      print(list_phone_numbers[name])
    else:
      print("no number")




