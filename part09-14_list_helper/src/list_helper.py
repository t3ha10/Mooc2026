# WRITE YOUR SOLUTION HERE:
class ListHelper:
  # def __init__(self):
  @classmethod
  def read_list(cls, my_list):
    freq_map = {}
    for number in my_list:
      if number in freq_map:
        freq_map[number] += 1
      else:
        freq_map[number] = 1
    return freq_map

  @classmethod
  def greatest_frequency(cls, my_list: list):
    freq_map = ListHelper.read_list(my_list)
    max_freq = 0
    greatest_freq = None
    for key, value in freq_map.items():
      if value > max_freq:
        max_freq = value
        greatest_freq = key

    return greatest_freq


  @classmethod
  def doubles(cls, my_list: list):
    freq_map = ListHelper.read_list(my_list)
    count = 0
    for key, value in freq_map.items():
      if value > 1:
        count += 1
    return count



if __name__ == "__main__":
  numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
  print(ListHelper.greatest_frequency(numbers))
  print(ListHelper.doubles(numbers))
  # 5
  # 3