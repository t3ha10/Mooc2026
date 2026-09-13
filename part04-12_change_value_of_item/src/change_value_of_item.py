# Write your solution here
list = [1, 2, 3, 4, 5]
i = 0
index = 0
while index != -1:
    index = int(input("Index:"))
    value_of_index = int(input("New value:"))
    list[index] = value_of_index
    print(list)
    i += 1
