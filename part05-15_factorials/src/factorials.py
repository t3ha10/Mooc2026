# Write your solution here
def factorials(n: int):
  box_factorials = {}
  for i in range(1, n + 1):
    box_factorials[i] = i
    for j in range(2, i):
      box_factorials[i] *= j
    
  return box_factorials


if __name__ == "__main__":
  k = factorials(5)
  print(k)
  print(k[1])
  print(k[3])
  print(k[5])
# 1
# 6
# 120