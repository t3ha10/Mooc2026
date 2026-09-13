# Write your solution here

while True:
  print("1 - add an entry, 2 - read entries, 0 - quit")
  function = int(input("Function: "))
  if function == 0:
    print("Bye now!")
    break

  if function == 1:
    entry = input("Diary entry: ")
    with open("diary.txt", "a") as diary_file:
      diary_file.write(entry + "\n")
      print("Diary saved\n")
  elif function == 2:
    print("Entries:")
    with open("diary.txt") as diary_file:
      for line in diary_file:
        print(line, end="")
    



