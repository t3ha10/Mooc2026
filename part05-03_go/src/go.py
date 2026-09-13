# Write your solution here
def who_won(game_board: list):
  amount_1 = 0
  amount_2 = 0

  for row in range(len(game_board)):
    for number in game_board[row]:
      if number == 1:
        amount_1 += 1
      elif number == 2:
        amount_2 += 1
  
  if amount_1 > amount_2:
    return 1
  elif amount_1 < amount_2:
    return 2
  else:
    return 0







if __name__ == "__main__":
  go = [
    [1, 0, 0, 0, 2, 0, 1, 0, 0], 
    [2, 0, 0, 2, 1, 0, 1, 0, 0],
    [0, 2, 0, 1, 0, 0, 0, 0, 2],
    [2, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 2]
  ]
  print(who_won(go))
  # 1: 12
  # 2: 9
