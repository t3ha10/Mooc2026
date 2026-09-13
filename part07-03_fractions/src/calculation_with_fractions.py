# Write your solution here
def fractionate(amount: int):
  from fractions import Fraction
  result = []
  for i in range(0, amount):
    result.append(Fraction(1, amount))
  return result



if __name__ == "__main__":
  for p in fractionate(3):
    print(p)
    print()
    print(fractionate(5))