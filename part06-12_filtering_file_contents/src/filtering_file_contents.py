# Write your solution here
def read_solutions_file():
  with open("solutions.csv") as new_file:
    solutions = []
    for line in new_file:
      solution = []
      parts = line.split(";")
      solution.append(parts[0])
      solution.append(parts[1])
      solution.append(int(parts[2]))
      solutions.append(solution)
    return solutions


def filter_solutions():
  solutions = read_solutions_file()
  open("correct.csv", "w").close()
  open("incorrect.csv", "w").close()
  for solution in solutions:
    operation = solution[1]

    line = (f"{solution[0]};{solution[1]};{solution[2]}\n")

    if operation.find("+") != -1:
      parts = operation.split("+")
      result = int(parts[0]) + int(parts[1])
      if result == solution[2]:
        with open("correct.csv", "a") as correct_file:
          correct_file.write(line)
      else:
        with open("incorrect.csv", "a") as incorrect_file:
          incorrect_file.write(line)


    if operation.find("-") != -1:
      parts = operation.split("-")
      result = int(parts[0]) - int(parts[1])
      if result == solution[2]:
        with open("correct.csv", "a") as correct_file:
          correct_file.write(line)
      else:
        with open("incorrect.csv", "a") as incorrect_file:
          incorrect_file.write(line)


    

if __name__ == "__main__":
  filter_solutions()