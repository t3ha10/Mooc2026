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
    
    if name not in list_phone_numbers:
      list_phone_numbers[name] = []
    list_phone_numbers[name].append(number)

    print("ok!")
  
  if command == 1:
    if name in list_phone_numbers:
      for i in list_phone_numbers[name]:
        print(i)
    else:
      print("no number")




