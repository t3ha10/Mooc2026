# Write your solution here
def throw_dice(list_sides):
  from random import randint
  return list_sides[randint(0, len(list_sides) - 1)]


def roll(die: str):
  dice = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]} 
  return throw_dice(dice[die])
  


def play(die1: str, die2: str, times: int):
  count_die1_win = 0
  count_die2_win = 0
  ties = 0
  for i in range(times):
    die1_result = roll(die1)
    die2_result = roll(die2)

    if die1_result > die2_result:
      count_die1_win += 1
    elif die1_result < die2_result:
      count_die2_win += 1
    else:
      ties += 1
  return count_die1_win, count_die2_win, ties



if __name__ == "__main__":
  for i in range(20):
    print(roll("A"), " ", end="")
  print()
  for i in range(20):
    print(roll("B"), " ", end="")
  print()
  for i in range(20):
    print(roll("C"), " ", end="")
  print()



  result = play("A", "C", 20)
  print(result)
  result = play("B", "B", 20)
  print(result)