# Write your solution here
list = []
amount = int(input("How many items:"))
i = 0
while i < amount:
    i += 1
 
    order = "Item " + str(i) + ": "
    number = int(input(order))
    list.append(number)
print(list)