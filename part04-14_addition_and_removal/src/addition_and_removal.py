# Write your solution here
print("The list is now []")
list =  []
request = ""
while request != "x":
  request = input("a(d)d, (r)emove or e(x)it:")
  if request == "d":
    list.append(len(list) + 1)
    print("The list is now",list)
  elif request == "r":
    list.pop(len(list) - 1)
    print("The list is now",list)

print("Bye!")  