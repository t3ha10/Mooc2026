# Write your solution here


def smallest_average(person1: dict, person2: dict, person3: dict):
  contestants = [person1, person2, person3]
  smallest_average_contestant = {}
  smallest_average_result = None
  for i in range(len(contestants)):
    average = (contestants[i]["result1"] + contestants[i]["result2"] + contestants[i]["result3"]) / 3
    if smallest_average_result == None:
      smallest_average_result = average
      smallest_average_contestant = contestants[i]
    else: 
      if smallest_average_result > average:
        smallest_average_result = average
        smallest_average_contestant = contestants[i]

  return smallest_average_contestant





if __name__ == "__main__":
  person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
  person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
  person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

  print(smallest_average(person1, person2, person3))