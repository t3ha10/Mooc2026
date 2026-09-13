# Write your solution here
from datetime import datetime

def read_file_start_times():
  start_times = {}
  with open("start_times.csv") as file:
    for line in file:
      line = line.replace("\n", "")
      parts = line.split(";")
      start_times[parts[0]] = parts[1]
  return start_times

def read_file_submissions():
  students_data = {}
  with open("submissions.csv") as file:
    for line in file:
      line = line.replace("\n", "")
      parts = line.split(";")
      results = []
      result = (int(parts[2]), parts[3])

      if parts[0] not in students_data:
        results.append(result)
        task = {}
        task[parts[1]] = results
        students_data[parts[0]] = task
      else:
        task = students_data[parts[0]]
        if parts[1] not in task:
          results.append(result)
          task[parts[1]] = results
        else:
          result = (int(parts[2]), parts[3])
          task[parts[1]].append(result)

  return students_data

def check_finish_time(start_time, obj_finish_times):
  # change start_time into hour
  start_time_real = datetime.strptime(start_time, "%H:%M")
  # process
  for task, finish_times_task in obj_finish_times.items():
    for tuple_result in finish_times_task:
      # change finish_time in tuple_result into hour
      finish_time = datetime.strptime(tuple_result[1], "%H:%M")

      # process
      delta = finish_time - start_time_real
      # change delta into hour:
      hours = delta.total_seconds() / 3600
      if hours > 3:
        return False
  return True

def cheaters():
  cheaters = []
  start_times = read_file_start_times()
  students_data = read_file_submissions()
  for name, start_time in start_times.items():
    obj_name = students_data[name]     
    if check_finish_time(start_time, obj_name) == False:
      cheaters.append(name)

  return cheaters

if __name__ == "__main__":
  # print(read_file_submissions())
  # students_data =  read_file_submissions()
  # print(read_file_start_times())
  # read_file_start_times()
  print(cheaters())
  # print(check_finish_time('17:01', students_data["arto"]))
