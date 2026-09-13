# Write your solution here


def print_persons(filename: str):
  import json
  with open(filename) as file:
    data = file.read()
  students = json.loads(data)
  for student in students:
    hobbies = ""
    for hobby in student["hobbies"]:
      hobbies = hobbies + hobby + ", "
    
    hobbies = hobbies[:-2]

    print(f'{student["name"]} {student["age"]} years ({hobbies})')

if __name__ == "__main__":
  print_persons("file1.json")
