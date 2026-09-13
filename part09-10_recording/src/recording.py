# WRITE YOUR SOLUTION HERE:
class Recording:
  def __init__(self, number):
    if number < 0:
      raise ValueError
    else:
      self.__length = number

  @property
  def length(self):
    return self.__length


  @length.setter
  def length(self, number):
    if number < 0:
      raise ValueError
    else:
      self.__length = number



if __name__ == "__main__":
  the_wall = Recording(-1)
  print(the_wall.length)
  the_wall.length = -1
  print(the_wall.length)