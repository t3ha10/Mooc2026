# Write your solution here
def hypotenuse(leg1: float, leg2: float):
  from math import sqrt
  expression = leg1 ** 2 + leg2 ** 2
  return sqrt(expression)


if __name__ == "__main__":
  print(hypotenuse(3,4)) # 5.0
  print(hypotenuse(5,12)) # 13.0
  print(hypotenuse(1,1)) # 1.4142135623730951