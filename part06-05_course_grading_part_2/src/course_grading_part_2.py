# write your solution here
# if False:
#   # this is never executed
#   student_info = input("Student information: ")
#   exercise_data = input("Exercises completed: ")
#   exam_data = input("Exam points: ")
# else:
#   # hard-coded input
#   student_info = "students1.csv"
#   exercise_data = "exercises1.csv"
#   exam_data = "exam_points1.csv"

if True:
  student_info = input("Student information: ")
  exercise_data = input("Exercises completed: ")
  exam_data = input("Exam points: ")

else:
  # now this is the False branch, and is never executed
  student_info = "students1.csv"
  exercise_data = "exercises1.csv"
  exam_data = "exam_points1.csv"


names = {}
with open(student_info) as students_file:
  for line in students_file:
    line = line.replace("\n", "")
    parts = line.split(";")
    if parts[0] == "id":
      continue
    names[parts[0]] = parts[1] + " " + parts[2]

exercise_points = {}
with open(exercise_data) as exercise_points_file:
  for line in exercise_points_file:
    parts = line.split(";")
    if parts[0] == "id":  
      continue

    points = 0
    for text in parts[1:]:
      point = int(text)
      points += point
    exercise_points[parts[0]] = points

converted_exercise_points = {}
for id_student, point in exercise_points.items():
  point = point // 4
  converted_exercise_points[id_student] = point

exam_points = {}
with open(exam_data) as exam_points_file:
  for line in exam_points_file:
    parts = line.split(";")
    if parts[0] == "id":  
      continue

    points = 0
    for text in parts[1:]:
      point = int(text)
      points += point
    exam_points[parts[0]] = points

grade_course = {28: 5, 24: 4, 21: 3, 18: 2, 15: 1, 0: 0}

for id_student, name in names.items():
  if id_student in converted_exercise_points:
    points = converted_exercise_points[id_student]

  if id_student in exam_points:
    points = points + exam_points[id_student]

  for key, grade in grade_course.items():
    if points >= key:
      student_grade = grade_course[key]
      break
  
  print(f"{name} {student_grade}")




