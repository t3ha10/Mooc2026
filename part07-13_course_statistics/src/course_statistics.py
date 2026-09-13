# Write your solution here
import urllib.request
import json
# import ssl


def read_data(course_name=None):
  if course_name == None:
  # if course_name is None:
    the_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
  else:
    the_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")

  data = the_request.read()
  courses = json.loads(data)
  return courses


def course_summary(course_data):
  total_exercises = sum(course_data["exercises"])
  return course_data["fullName"], course_data["name"], course_data["year"], total_exercises



def retrieve_all():
  data = read_data()
  active_courses = []
  for course_data in data:
    if course_data["enabled"] == True:
      active_course = course_summary(course_data)
      active_courses.append(active_course)
  return active_courses

def get_info_courses(data):
  course_name_data = []
  for course_number, info in data.items():
    course_name_data.append(info)
  return course_name_data



def retrieve_course(course_name: str):
  data = read_data(course_name)
  course_info = {}
  course_name_data = get_info_courses(data)
  course_info['weeks'] = len(course_name_data)
  students = 0
  hours = 0
  exercises = 0
  for i in course_name_data:
    if i["students"] > students:
      students = i["students"]
    hours += i["hour_total"]
    exercises += i["exercise_total"]


  course_info['students'] = students
  course_info['hours'] = hours
  course_info['hours_average'] = hours // students
  course_info['exercises'] = exercises
  course_info['exercises_average'] = exercises // students

  return course_info

if __name__ == "__main__":
 print(retrieve_course("docker2019"))
  
