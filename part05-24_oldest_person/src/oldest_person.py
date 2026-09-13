# Write your solution here
def oldest_person(people: list):
  oldest_year = people[0][1]
  name_of_oldest_person = people[0][0]
  for i in range(len(people)):
    years_old = people[i][1]
    if years_old < oldest_year:
      oldest_year = years_old
      name_of_oldest_person = people[i][0]

  return name_of_oldest_person



if __name__ == "__main__":
  p1 = ("Adam", 1977)
  p2 = ("Ellen", 1985)
  p3 = ("Mary", 1953)
  p4 = ("Ernest", 1997)
  people = [p1, p2, p3, p4]

  print(oldest_person(people))
  # Mary