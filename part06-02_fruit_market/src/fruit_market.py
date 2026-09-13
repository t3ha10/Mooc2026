# write your solution here
def read_fruits():
  with open("fruits.csv") as list_prices:
    fruits_price = {}
    for line in list_prices:
      fruit_price = line.split(";")
      fruit = fruit_price[0]
      price = float(fruit_price[1])
      fruits_price[fruit] = price
    return fruits_price



if __name__ == "__main__":
  print(read_fruits())