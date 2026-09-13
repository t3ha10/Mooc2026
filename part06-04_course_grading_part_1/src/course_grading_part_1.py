# write your solution here
# if False:
#   # this is never executed
#   student_info = input("Student information: ")
#   exercise_data = input("Exercises completed: ")
# else:
#   # hard-coded input
#   student_info = "students1.csv"
#   exercise_data = "exercises1.csv"
if True:
  student_info = input("Student information: ")
  exercise_data = input("Exercises completed: ")
else:
  # now this is the False branch, and is never executed
  student_info = "students1.csv"
  exercise_data = "exercises1.csv"


names = {}
with open(student_info) as students_file:
  for line in students_file:
    line = line.replace("\n", "")
    parts = line.split(";")
    if parts[0] == "id":
      continue
    names[parts[0]] = parts[1] + " " + parts[2]

points = {}
with open(exercise_data) as exercises_file:
  for line in exercises_file:
    parts = line.split(";")
    if parts[0] == "id":
      continue
    
    numbers = 0
    for text in parts[1:]:
      number = int(text)
      numbers += number
    points[parts[0]] = numbers
  





for id_student, name in names.items():
  if id_student in points:
    point = points[id_student]
  print(f"{name} {point}")



