# WRITE YOUR SOLUTION HERE:
class SimpleDate:
  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year

  def calculate(self):
    result = str(self.year)
    if self.month < 10:
      result = result + "0" + str(self.month)
    else:
      result += str(self.month)
    
    if self.day < 10:
      result = result + "0" + str(self.day)
    else:
      result += str(self.day)

    return int(result)
  
  def __eq__(self, another):
    return self.calculate() == another.calculate()
  def __ne__(self, another):
    return self.calculate() != another.calculate()
  def __lt__(self, another):
    return self.calculate() < another.calculate()
  def __gt__(self, another):
    return self.calculate() > another.calculate()

  def __add__(self, number):
    superfluous_day = number % 30
    month_add = number // 30
    superfluous_month = month_add % 12
    year_add = month_add // 12
    new_day = 0
    new_month = 0
    new_year = 0

    if superfluous_day + self.day > 30:
      new_day = superfluous_day + self.day - 30
      new_month += 1
    else:
      new_day = superfluous_day + self.day
    
    if superfluous_month + self.month > 12:
      new_month += superfluous_month + self.month - 12
      new_year += 1
    else:
      new_month += superfluous_month + self.month
    
    new_year = new_year + self.year + year_add
    return SimpleDate(new_day, new_month, new_year)

  def __sub__(self, another):
    days = 0
    day_difference = (self.day - another.day) + 30 * (self.month - another.month) + 30 * 12 * (self.year - another.year)
    days += abs(day_difference)
    return days
    
  def __str__(self):
    return f"{self.day}.{self.month}.{self.year}"

if __name__ == "__main__":
  d1 = SimpleDate(4, 10, 2020)
  d2 = SimpleDate(2, 11, 2020)
  d3 = SimpleDate(28, 12, 1985)

  print(d2-d1)
  print(d1-d2)
  print(d1-d3)