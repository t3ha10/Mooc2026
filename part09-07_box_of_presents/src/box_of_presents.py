# WRITE YOUR SOLUTION HERE:
class Present:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def __str__(self):
    return f"{self.name} ({self.weight} kg)"



class Box:
  def __init__(self):
    self.boxes = []

  def add_present(self, present: Present):
    self.boxes.append(present)


  def total_weight(self):
    total = 0
    for i in self.boxes:
      total += i.weight
    return total


if __name__ == "__main__":
  book = Present("ABC Book", 2)

  print("The name of the present:", book.name)
  print("The weight of the present:", book.weight)
  print("Present:", book)


  box = Box()
  box.add_present(book)
  print(box.total_weight())

  cd = Present("Pink Floyd: Dark Side of the Moon", 1)
  box.add_present(cd)
  print(box.total_weight())