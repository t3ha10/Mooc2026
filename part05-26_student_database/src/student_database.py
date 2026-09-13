# Write your solution here
# add a new student to the database
def add_student(students, name):
  students[name] = []

def check_student_exists(students, name):
  return name in students

# Input: >..
# Output: True if student already has the said course. Otherwise, false
def check_course_exists_for_student(student_courses, course_name):
  for i in student_courses:
    if course_name == i[0]:
      return True
  return False

# input: ...
# output: ...
def add_course(students, name, new_course):
  # 1. Check exists before add
  if not check_student_exists(students, name):
    add_student(students, name)
  
  # 2. Only add if new course has grade > 0
  new_course_grade = new_course[1]
  if new_course_grade == 0:
    return
  
  # 3. Add new course

  # - Only add course if student does not have one yet
  # - Check exist course
  student_courses = students[name]
  new_course_name = new_course[0]
  already_has_course = check_course_exists_for_student(student_courses, new_course_name)

  if not already_has_course:
    student_courses.append(new_course)
    return
  
  # - Replace/Update grade if student already has course
  for index in range(len(student_courses)):
    student_course = student_courses[index]
    if student_course[0] == new_course_name and student_course[1] < new_course_grade:
      student_courses[index] = new_course
      return

def calculate_average(student_courses):
  average_grade = 0
  for i in student_courses:
    average_grade += i[1]
  average_grade /= len(student_courses) 
  return average_grade

def print_courses(student_courses):
  for i in student_courses:
    print(f"  {i[0]} {i[1]}")


def print_student(students, name):
  if name not in students:
    print(f"{name}: no such person in the database")
  elif students[name] == []:
    print(f"{name}:\n no completed courses")
  else:
    student_courses = students[name]
    print(f"{name}:\n {len(student_courses)} completed courses:")
    print_courses(student_courses)
    average_grade = calculate_average(student_courses)
    print(f" average grade {average_grade}")

def summary(students):
  # students 2
  print(f"students {len(students)}")

  # most courses completed 3 Peter
  # best average grade 4.5 Eliza

  most_courses = 0
  most_courses_name = ""
  best_average_grade = 0
  best_average_grade_name = ""
  for name, courses in students.items():
    if len(courses) > most_courses:
      most_courses = len(courses)
      most_courses_name = name

    if calculate_average(courses) > best_average_grade:
      best_average_grade = calculate_average(courses)
      best_average_grade_name = name

  print(f"most courses completed {most_courses} {most_courses_name}")
  print(f"best average grade {best_average_grade} {best_average_grade_name}")






if __name__ == "__main__":
  students = {}
  add_student(students, "Peter")
  add_student(students, "Eliza")
  add_course(students, "Peter", ("Introduction to Programming", 3))
  add_course(students, "Peter", ("Advanced Course in Programming", 2))
  add_course(students, "Peter", ("Introduction to Programming", 4))
  add_course(students, "Peter", ("Advanced Course in Programming", 5))
  add_course(students, "Peter", ("Data Structures and Algorithms", 0))
  add_course(students, "Peter", ("Introduction to Programming", 2))
  add_course(students, "Peter", ("Data Structures and Algorithms", 1))
  add_course(students, "Peter", ("Introduction to Programming", 1))
  add_course(students, "Peter", ("Advanced Course in Programming", 1))
  add_course(students, "Eliza", ("Introduction to Programming", 5))
  add_course(students, "Eliza", ("Introduction to Computer Science", 4))

  print_student(students, "Peter")
  print_student(students, "Eliza")
  print_student(students, "Jack")
  summary(students)

  