# Write your solution here:
class Item:
  def __init__(self, name, weight):
    self.__name = name
    self.__weight = weight
  
  def name(self):
    return self.__name

  def weight(self):
    return self.__weight

  def __str__(self):
    return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
  def __init__(self, max_weight):
    self.max_weight = max_weight
    self.__list_items = []

  def check_current_weight(self):
    if len(self.__list_items) == 0:
      return 0
    
    result = 0
    for item in self.__list_items:
      result += item.weight()
    return result

  def add_item(self, added_item: Item):
    if self.check_current_weight() + added_item.weight() < self.max_weight:
      self.__list_items.append(added_item)

  def print_items(self):
    for item in self.__list_items:
      print(item)

  def weight(self):
    return self.check_current_weight()

  def heaviest_item(self):
    if len(self.__list_items) == 0:
      return None
    
    found_item = None
    for item in self.__list_items:
      if found_item == None or item.weight() > found_item.weight():
        found_item = item
    return found_item

  def __str__(self):
    if len(self.__list_items) == 1:
      return f"1 item ({self.weight()} kg)"
    else: 
      return f"{len(self.__list_items)} items ({self.weight()} kg)"

class CargoHold:
  def __init__(self, max_weight):
    self.max_weight = max_weight
    self.__list_suitcases = []

  def check_total_weight(self):
    if len(self.__list_suitcases) == 0:
      return 0
    result = 0
    for item in self.__list_suitcases:
      result += item.weight()
    return result

  def add_suitcase(self, suitcase: Suitcase):
    if self.check_total_weight() + suitcase.weight() < self.max_weight:
      self.__list_suitcases.append(suitcase)

  def print_items(self):
    for suitcase in self.__list_suitcases:
      suitcase.print_items()

  def __str__(self):
    if len(self.__list_suitcases) == 1:
      return f"1 suitcase, space for {self.max_weight - self.check_total_weight()} kg"
    return f"{len(self.__list_suitcases)} suitcases, space for {self.max_weight - self.check_total_weight()} kg"


if __name__ == "__main__":
  cargo_hold = CargoHold(1000)
  print(cargo_hold)

  book = Item("ABC Book", 2)
  phone = Item("Nokia 3210", 1)
  brick = Item("Brick", 4)

  adas_suitcase = Suitcase(10)
  adas_suitcase.add_item(book)
  adas_suitcase.add_item(phone)

  peters_suitcase = Suitcase(10)
  peters_suitcase.add_item(brick)

  cargo_hold.add_suitcase(adas_suitcase)
  print(cargo_hold)

  cargo_hold.add_suitcase(peters_suitcase)
  print(cargo_hold)


  print("The suitcases in the cargo hold contain the following items:")
  cargo_hold.print_items()
  # 0 suitcases, space for 1000 kg
  # 1 suitcase, space for 997 kg
  # 2 suitcases, space for 993 kg
  # The suitcases in the cargo hold contain the following items:
  # ABC Book (2 kg)
  # Nokia 3210 (1 kg)
  # Brick (4 kg)