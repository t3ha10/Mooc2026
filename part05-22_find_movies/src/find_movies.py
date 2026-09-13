# Write your solution here
def find_movies(database: list, search_term: str):
  list_found = []
  for i in range(len(database)):
    search_item = database[i]["name"].lower()
    if search_item.find(search_term) != -1:
      list_found.append(database[i])
  return list_found



if __name__ == "__main__":
  database = [
    {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
    ]

  my_movies = find_movies(database, "python")

  print(my_movies)
  # [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, 
  # {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]