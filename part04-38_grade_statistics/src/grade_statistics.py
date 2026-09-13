# Write your solution here


# Input: none
# Output: [ [5, 14], [10, 100] ]
# Description: 
def users_input():
  list_inputs = []
  while True:
    user_input = input("Exam points and exercises completed: ")
    if user_input == "":
      return list_inputs

    input_pair = user_input.split()
    exam_point = int(input_pair[0])
    exercise_point = int(input_pair[1]) // 10

    list_inputs.append([exam_point, exercise_point])



def check_threshold_fail(list_points):
  list_convert_fail = list_points
  for i in list_convert_fail:
    if i[0] < 10:
      i[0] = 0
  return list_convert_fail






def convert_general_points(my_list):
  general_points = []
  for i in my_list:
    i = int(i[0]) + i[1]
    general_points.append(i)
  return general_points





# Input: point
# Output: grade

def get_grade(point):
  lookup = [28, 24, 21, 18, 15, 0]
  grades = [ 5,  4,  3,  2,  1, 0]

  for index in range(len(lookup) - 1):
    if point >= lookup[index]:
      return grades[index]
  
  return 0


def convert_grades(my_list):
  grades = []
  
  for i in my_list:
    grade = get_grade(i)
    grades.append(grade)
  
  return grades
      
def count_average(my_list):
  return sum(my_list) / len(my_list)



def pass_percentage(list_grades):
  fail_amounts = list_grades.count(0)
  pass_percent = 100 - (fail_amounts /len(list_grades)) * 100
  return pass_percent

def count_amount_grades(list_grades):
  amount_grades = [0, 0, 0, 0, 0, 0]

  for i in list_grades:
    amount_grades[i] += 1

   
  return amount_grades




def grade_distribution(amount_grades):


  for i in range(5,0-1,-1):
    print(f"{i:>3}: {amount_grades[i]*'*':3}")






list_points = users_input()
list_general_points = convert_general_points(list_points)

print("Statistics:")
# print(list_points)
# print(list_general_points)
print(f"Points average:", count_average(list_general_points))


list_threshold_fails = convert_general_points(check_threshold_fail(list_points))

list_grades = convert_grades(list_threshold_fails)

# print(check_threshold_fail(list_points))
# print(list_grades)

print(f"Pass percentage:{pass_percentage(list_grades): .1f}")
print("Grade distribution:")
grade_users = count_amount_grades(list_grades)
grade_distribution(grade_users)













# the "main function" using these functions
