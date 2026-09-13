# Write your solution here
item = None
list = []
while item != 0:
  item = int(input("New item: "))
  if item == 0:
    break
  list.append(item)
  print("The list now:",list)
  print("The list in order:",sorted(list))
print("Bye!")