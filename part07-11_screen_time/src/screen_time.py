# Write your solution here
from datetime import datetime, timedelta
one_day = timedelta(days=1)

def format_date(day):
  return day.strftime("%d.%m.%Y")

def process_time_by_day(str):
  numbers = []
  numbers_text = str.split(" ")
  for number in numbers_text:
    numbers.append(int(number))
  return numbers

def main():
  filename = input("Filename: ")
  starting_date_text = input("Starting date: ")
  number_of_days_text = input("How many days: ")
  
  # parse starting_date_text into datetime
  starting_date = datetime.strptime(starting_date_text, "%d.%m.%Y")
  number_of_days = int(number_of_days_text)
  finish_date = starting_date + (number_of_days -1) * one_day
  print("Please type in screen time in minutes on each day (TV computer mobile):")


  with open(filename, "w") as new_file:
    new_file.write(f"Time period: {format_date(starting_date)}-{format_date(finish_date)}\n")


    total_minutes = 0
    screen_time_by_day = {}
    for i in range(number_of_days):
      day = starting_date + i * one_day
      format_day = format_date(day)
      spent_time = input(f"Screen time {format_day}: ")
      screen_time_by_day[format_day] = process_time_by_day(spent_time)
      total_minutes += sum(process_time_by_day(spent_time))
    
    
    new_file.write(f"Total minutes: {total_minutes}\n")
    new_file.write(f"Average minutes: {total_minutes / number_of_days}\n")
    for day, spent_time in screen_time_by_day.items():

      format_spent_time = ""
      for minutes in spent_time:
        format_spent_time = format_spent_time + str(minutes) + "/"
      new_file.write(f"{day}: {format_spent_time[:-1]}\n")

  print(f"Data stored in file {filename}")
  

main()