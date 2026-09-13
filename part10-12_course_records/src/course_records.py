# tee ratkaisusi tänne
class CourseData:
  def __init__(self):
    self.__courses = {}

  def add_grade(self, name, grade: int, credit: int):
    if not name in self.__courses:
      self.__courses[name] = {}
      self.__courses[name]["grade"] = grade
    else:
      current_grade = self.__courses[name]["grade"]
      if current_grade < grade:
        self.__courses[name]["grade"] = grade
      
    self.__courses[name]["credit"] = credit

  def get_course(self, name):
    if not name in self.__courses:
      return None
    return self.__courses[name]
  
  def completed_course_count(self):
    return len(self.__courses)

  def get_total_by(self, attribute_name: str):
    result = 0
    for course in self.__courses.values():
      result += course[attribute_name]
    return result

  def mean_course(self):
    total_grade = self.get_total_by("grade")
    total_courses = self.completed_course_count()
    if total_courses == 0:
      return 0
    return f"{total_grade/total_courses:.1f}"

  def grade_distribution(self):
    table_grade = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for course in self.__courses.values():
      grade = course["grade"]
      table_grade[grade] += 1
    return table_grade

  def all_entries(self):
    return self.__courses

class CourseDataApplication:
  def __init__(self):
    self.__coursedata = CourseData()

  def help(self):
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")

  def add_course(self):
    name = input("course: ")
    grade = input("grade: ")
    credit = input("credits: ")
    self.__coursedata.add_grade(name, int(grade), int(credit))

  def get_course_data(self):
    name = input("course: ")
    info = self.__coursedata.get_course(name)
    if info == None:
      print("no entry for this course")
    else:
      print(f"{name} ({info["credit"]} cr) grade {info["grade"]}")

  def statistics(self):
    print(f"{self.__coursedata.completed_course_count()} completed courses, a total of {self.__coursedata.get_total_by("credit")} credits")
    print(f"mean {self.__coursedata.mean_course()}")
    print("grade distribution")
    for key, value in self.__coursedata.grade_distribution().items():
      print(f"{key}: {value * "x"}")
    
  def execute(self):
    self.help()
    while True:
      print("")
      command = input("command: ")
      if command =="0":
        break
      elif command == "1":
        self.add_course()
      elif command == "2":
        self.get_course_data()
      elif command == "3":
        self.statistics()
      else:
        self.help()

application = CourseDataApplication()
application.execute()

