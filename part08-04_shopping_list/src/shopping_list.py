# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------
def total_units(my_list: ShoppingList):
    result = 0
    for i in range(1, my_list.number_of_items()+1):
        item = my_list.item(i)
        amount = my_list.amount(i)
        result += amount
    return result

if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)
    print(total_units(shopping_list)) 
    # 16

    print(shopping_list.number_of_items())
    print(shopping_list.item(1), shopping_list.amount(1))
    print()
    print(shopping_list.item(2), shopping_list.amount(2))
    print()
    # 3
    # bananas 10

    # apples 5

    # the items on the shopping list are indexed from 1
    for i in range(1, shopping_list.number_of_items()+1):
        item = shopping_list.item(i)
        amount = shopping_list.amount(i)
        print(f"{item}: {amount} units")
     
    # bananas: 10 units
    # apples: 5 units
    # pineapple: 1 units 