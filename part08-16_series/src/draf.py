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
  print(shopping_list.item(2), shopping_list.amount(2))
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

# -----------------------------
# 
# -----------------------------

class Book:
def __init__(self, name: str, author: str, genre: str, year: int):
  self.name = name
  self.author = author
  self.genre = genre 
  self.year = year

def older_book(book1: Book, book2: Book):
  year1 = book1.year
  year2 = book2.year
  if year1 < year2:
      print(f"({book1.name} is older, it was published in {year1})")
  elif year1 == year2:
      print(f"({book1.name} and {book2.name} were published in {year1})")
  else:
      print(f"({book2.name} is older, it was published in {year2})")

if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)
# -----------------------------
# 
# -----------------------------

class Book:
  def __init__(self, name: str, author: str, genre: str, year: int):
    self.name = name
    self.author = author
    self.genre = genre 
    self.year = year

  ##STUB:# This enables easy printing of a Book object
  def __repr__(self):
    return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"

def books_of_genre(books: list, genre: str):
  found_book = []

  for i in range(len(books)):
    if books[i].genre == genre:
        found_book.append(books[i])
  return found_book
if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")

# -----------------------------
# 
# -----------------------------


class Pet:

  def __init__(self, name, species, year_of_birth):
    self.name = name
    self.species = species
    self.year_of_birth = year_of_birth

def new_pet(name: str, species: str, year_of_birth: int):
  new_pet = Pet(name, species, year_of_birth)
  return new_pet


if __name__ == "__main__":
  fluffy = new_pet("Fluffy", "dog", 2017)
  print(fluffy.name)
  print(fluffy.species)
  print(fluffy.year_of_birth)

# -----------------------------
# 
# -----------------------------

from datetime import date
class PersonalBest:
  def __init__(self, player: str, day: int, month: int, year: int, points: int):
      # Default values
      self.player = ""
      self.date_of_pb = date(1900, 1, 1)
      self.points = 0

      if self.name_ok(player):
          self.player = player

      if self.date_ok(day, month, year):
          self.date_of_pb = date(year, month, day)

      if self.points_ok(points):
          self.points = points

  # Helper methods to check the arguments are valid
  def name_ok(self, name: str):
      return len(name) >= 2 # Name should be at least two characters long

  def date_ok(self, day, month, year):
      try:
          date(year, month, day)
          return True
      except:
          # an exception is raised if the arguments are not valid
          return False

  def points_ok(self, points):
      return points >= 0

if __name__ == "__main__":
  result1 = PersonalBest("Peter", 1, 11, 2020, 235)
  print(result1.points)
  print(result1.player)
  print(result1.date_of_pb)

  # The date was not valid
  result2 = PersonalBest("Paula", 4, 13, 2019, 4555)
  print(result2.points)
  print(result2.player)
  print(result2.date_of_pb) # Tulostaa oletusarvon 1900-01-01

# -----------------------------
# 
# -----------------------------
class BonusCard:
  def __init__(self, name: str, balance: float):
    self.name = name
    self.balance = balance

  def add_bonus(self):
    # The variable bonus below is a local variable.
    # It is not a data attribute of the object.
    # It can not be accessed directly through the object.
    bonus = self.balance * 0.25
    self.balance += bonus

  def add_superbonus(self):
    # The superbonus variable is also a local variable.
    # Usually helper variables are local variables because
    # there is no need to access them from the other
    # methods in the class or directly through an object.
    superbonus = self.balance * 0.5
    self.balance += superbonus

  def __str__(self):
    return f"BonusCard(name={self.name}, balance={self.balance})"
# -----------------------------
# 
# -----------------------------

class Rectangle:
  def __init__(self, left_upper: tuple, right_lower: tuple):
    self.left_upper = left_upper
    self.right_lower = right_lower
    self.width = right_lower[0]-left_upper[0]
    self.height = right_lower[1]-left_upper[1]

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return self.width * 2 + self.height * 2

  def move(self, x_change: int, y_change: int):
    corner = self.left_upper
    self.left_upper = (corner[0]+x_change, corner[1]+y_change)
    corner = self.right_lower
    self.right_lower = (corner[0]+x_change, corner[1]+y_change)
  
  # This method returns the state of the object in string format
  def __str__(self):
    return f"rectangle {self.left_upper} ... {self.right_lower}"

rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)



rectangle = Rectangle((1, 1), (4, 3))
str_rep = str(rectangle)
print(str_rep)
# -----------------------------
# 
# -----------------------------
class TaskList:
  def __init__(self):
    self.tasks = []

  def add_task(self, name: str, priority: int):
    self.tasks.append((priority, name))

  def get_next(self):
    self.tasks.sort()
    # The list method pop removes and returns the last item in a list
    task = self.tasks.pop()
    # Return the name of the task (the second item in the tuple)
    return task[1]

  def number_of_tasks(self):
    return len(self.tasks)

  def clear_tasks(self):
    self.tasks = []