# tee ratkaisu tänne
if True:
  student_info = input("Student information: ")
  exercise_data = input("Exercises completed: ")
  exam_data = input("Exam points: ")
  course_info = input("Course information: ")

else:
  student_info = "students1.csv"
  exercise_data = "exercises1.csv"
  exam_data = "exam_points1.csv"
  course_info = "course1.txt"



open("results.txt", "w").close()
open("results.csv", "w").close()


names = {}
with open(student_info) as students_file:
  for line in students_file:
    line = line.replace("\n", "")
    parts = line.split(";")
    if parts[0] == "id":
      continue
    names[parts[0]] = parts[1] + " " + parts[2]

exercise_points = {}
with open(exercise_data) as exercise_file:
  for line in exercise_file:
    parts = line.split(";")
    if parts[0] == "id":
      continue
    
    numbers = 0
    for text in parts[1:]:
      number = int(text)
      numbers += number
    
    exercise_points[parts[0]] = numbers

converted_exercise_point = {}
for id_student, number in exercise_points.items():
  point = number // 4
  converted_exercise_point[id_student] = point

exam_points = {}
with open(exam_data) as exam_file:
  for line in exam_file:
    parts = line.split(";")
    if parts[0] == "id":
      continue

    point = 0
    for text in parts[1:]:
      number = int(text)
      point += number
    exam_points[parts[0]] = point


grade_table = {28: 5, 24: 4, 21: 3, 18: 2, 15: 1, 0: 0}

course_data = []
course_data.append(["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"])
for id_student, name in names.items():
  student = []
  student.append(name)
  if id_student in exercise_points:
    student.append(str(exercise_points[id_student]))
  if id_student in converted_exercise_point:
    exec_pts = str(converted_exercise_point[id_student])
    student.append(exec_pts)
  if id_student in exam_points:
    exm_pts = str(exam_points[id_student])
    student.append(exm_pts)

  total_points = int(exec_pts) + int(exm_pts)
  student.append(str(total_points))
  for point, grade in grade_table.items():
    if total_points >= point:
      student.append(str(grade_table[point]))
      break


  
  course_data.append(student)

course_info_data = []
with open(course_info) as course_info_file:
  for line in course_info_file:
    line = line.replace("\n", "")
    parts = line.split(": ")
    course_info_data.append(parts[1])


with open("results.txt", "a") as result_table_file:
  course_info_line = f"{course_info_data[0]}, {course_info_data[1]} credits"
  decor = len(course_info_line) * "="

  result_table_file.write(course_info_line+"\n")
  result_table_file.write(decor+"\n")
  for row in range(len(course_data)):
    recipe = ""
    for col in range(len(course_data[row])):
      if col == 0:
        recipe += f"{course_data[row][col]:30}"
        if course_data[row][0] == "name":
          continue
        else:
          with open("results.csv", "a") as result_file:
            for id_student, name in names.items():
              if name == course_data[row][0]:
                result_file.write(f"{id_student};{name};{course_data[row][len(course_data[row]) - 1]}\n")


      else:
        recipe += f"{course_data[row][col]:10}" 
  
    result_table_file.write(recipe+"\n")

print("Results written to files results.txt and results.csv")
      