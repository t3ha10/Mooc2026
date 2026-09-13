# ________________#
class Person:
   def __init__(self, name: str, email: str):
       self.name = name
       self.email = email
   def update_email_domain(self, new_domain: str):
       old_domain = self.email.split("@")[1]
       self.email = self.email.replace(old_domain, new_domain)
class Student(Person):
   def __init__(self, name: str, id: str, email: str, credits: str):
       self.name = name
       self.id = id
       self.email = email
       self.credits = credits
class Teacher(Person):
   def __init__(self, name: str, email: str, room: str, teaching_years: int):
       self.name = name
       self.email = email
       self.room = room
       self.teaching_years = teaching_years

# ________________#
class Book:
   """ This class models a simple book """
   def __init__(self, name: str, author: str):
       self.name = name
       self.author = author
class BookContainer:
   """ This class models a container for books """
   def __init__(self):
       self.books = []
   def add_book(self, book: Book):
       self.books.append(book)
   def list_books(self):
       for book in self.books:
           print(f"{book.name} ({book.author})")
class Bookshelf(BookContainer):
   """ This class models a shelf for books """
   def __init__(self):
       super().__init__()
   def add_book(self, book: Book, location: int):
       self.books.insert(location, book)
class Thesis(Book):
    """ This class models a graduate thesis """
    def __init__(self, name: str, author: str, grade: int):
        super().__init__(name, author)
        self.grade = grade


# ________________#
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
class BonusCard:
    def __init__(self):
        self.products_bought = []
    def add_product(self, product: Product):
        self.products_bought.append(product)
    def calculate_bonus(self):
        bonus = 0
        for product in self.products_bought:
            bonus += product.price * 0.05
        return bonus
class PlatinumCard(BonusCard):
    def __init__(self):
        super().__init__()
    def calculate_bonus(self):
        # Call the method in the base class
        bonus = super().calculate_bonus()
        # ...and add five percent to the total
        bonus = bonus * 1.05
        return bonus



# ________________#
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed
    @property
    def model(self):
        return self.__model
    @property
    def speed(self):
        return self.__speed
class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.weight = weight
    def __str__(self):
        return f"{super().model}, {super().speed} MHz, {self.weight} kg"
if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2) 
    print(laptop) 

# ________________#
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year
class GameWarehouse:
    def __init__(self):
        self.__games = []
    def add_game(self, game: ComputerGame):
        self.__games.append(game)
    def list_games(self):
        return self.__games
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
    def list_games(self):
        request_year = 1990
        games = []
        # games = super().list_games()
        for game in super().list_games():
            if game.year < request_year:
                games.append(game)   
        return games

# ________________#
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    def __str__(self):
        return f"rectangle {self.width}x{self.height}"
    def area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length
    def __str__(self):
        return f"square {self.width}x{self.height}"

# ________________#
class Notebook:
    """ A Notebook stores notes in string format """

    def __init__(self):
        # protected attribute
        self._notes = []

    def add_note(self, note):
        self._notes.append(note)

    def retrieve_note(self, index):
        return self._notes[index]

    def all_notes(self):
        return ",".join(self._notes)

class NotebookPro(Notebook):
    """ A better Notebook with search functionality """
    def __init__(self):
        # This is OK, the constructor is public despite the underscores
        super().__init__()

    # This works, the protected attribute is accessible to the derived class
    def find_notes(self, search_term):
        found = []
        for note in self._notes:
            if search_term in note:
                found.append(note)

        return found
        
# ________________#
class Person:
    def __init__(self, name: str):
        self._name = self._capitalize_initials(name)

    def _capitalize_initials(self, name):
        name_capitalized = []
        for n in name.split(" "):
            name_capitalized.append(n.capitalize())

        return " ".join(name_capitalized)

    def __repr__(self):
        return self.__name

class Footballer(Person):

    def __init__(self, name: str, nickname: str, position: str):
        super().__init__(name)
        # the method is available as it is protected in the base class
        self.__nickname = self._capitalize_initials(nickname)
        self.__position = position

    def __repr__(self):
        r =  f"Footballer - name: {self._name}, nickname: {self.__nickname}"
        r += f", position: {self.__position}"
        return r

# Test the classes
if __name__ == "__main__":
    jp = Footballer("peter pythons", "pyper", "forward")
    print(jp)

# ________________#
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    def product_on_sale(self):
        on_sale = Product(self.__name, self.__price * 0.75)
        return on_sale

# ________________#
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def cheaper(self, Product):
        if self.__price < Product.price:
            return self
        else:
            return Product
            
# ________________#
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def __gt__(self, another_product):
        return self.price > another_product.price

# ________________#
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    def __gt__(self, another_product):
        return self.name > another_product.name

# ________________#
from datetime import datetime

class Note:
    def __init__(self, entry_date: datetime, entry: str):
        self.entry_date = entry_date
        self.entry = entry

    def __str__(self):
        return f"{self.entry_date}: {self.entry}"

    def __add__(self, another):
        # The date of the new note is the current time
        new_note = Note(datetime.now(), "")
        new_note.entry = self.entry + " and " + another.entry
        return new_note

entry1 = Note(datetime(2016, 12, 17), "Remember to buy presents")
entry2 = Note(datetime(2016, 12, 23), "Remember to get a tree")

# These notes can be added together with the + operator
# This calls the  __add__ method in the Note class
both = entry1 + entry2
print(both)
# ________________#
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"
person1 = Person("Anna", 25)
person2 = Person("Peter", 99)
print(person1)
print(person2)
# Person('Anna', 25)
# Person('Peter', 99)

# ________________#
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age} years)"
Person = Person("Anna", 25)
print(Person)
print(repr(Person))
# Anna (25 years)
# Person('Anna', 25)

# ________________#
class Book:
    def __init__(self, name: str, author: str, page_count: int):
        self.name = name
        self.author = author
        self.page_count = page_count

class Bookshelf:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    # This is the iterator initialization method
    # The iteration variable(s) should be initialized here
    def __iter__(self):
        self.n = 0
        # the method returns a reference to the object itself as 
        # the iterator is implemented within the same class definition
        return self

    # This method returns the next item within the object
    # If all items have been traversed, the StopIteration event is raised
    def __next__(self):
        if self.n < len(self._books):
            # Select the current item from the list within the object
            book = self._books[self.n]
            # increase the counter (i.e. iteration variable) by one
            self.n += 1
            # return the current item
            return book
        else:
            # All books have been traversed
            raise StopIteration
b1 = Book("The Life of Python", "Montague Python", 123)
b2 = Book("The Old Man and the C", "Ernest Hemingjavay", 204)
b3 = Book("A Good Cup of Java", "Caffee Coder", 997)

shelf = Bookshelf()
shelf.add_book(b1)
shelf.add_book(b2)
shelf.add_book(b3)

# Print the names of all the books
for book in shelf:
    print(book.name)
# The Life of Python
# The Old Man and the C
# A Good Cup of Java

# ________________#
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None

        return self.__persons[name]


    # return all entries (in dictionary format)
    def all_entries(self):
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    # the rest of the program
class PhoneBookApplication:
    # the rest of the code for the user interface

    # a method which gets executed as the program exits
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":

                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")


    # separation of concerns in action: a new method for adding an entry
    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                # name = input("name: ")
                # number = input("number: ")
                # self.__phonebook.add_number(name, number)
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()

class FileHandler:
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers

        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")



# code for testing
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_numbers("Eric"))
print(phonebook.get_numbers("Emily"))
application = PhoneBookApplication()
application.execute()
my_list = [1, 2, 3, 4, 5]
first, second, *rest = my_list
print(first)
print(second)
print(rest)
t = FileHandler("phonebook.txt")
print(t.load_file())

# ['02-123456']
# None
# commands:
# 0 exit
# 1 add entry
# 2 search

# command: 1
# name: Eric
# number: 02-123456

# command: 1
# name: Eric
# number: 045-4356713

# command: 2
# name: Eric
# 02-123456
# 045-4356713

# command: 2
# name: Emily
# number unknown

# command: 0


# 1
# 2
# [3, 4, 5]
# {'Eric': ['02-1234567', '045-4356713'], 'Emily': ['040-324344']}

# ________________#
# ________________#
# ________________#
# ________________#
# ________________#
# ________________#
# ________________#
# ________________#
# ________________#
# ________________#
