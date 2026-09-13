# Write your solution here
def copy_file(filename):
  list_copy = []
  with open(filename) as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      list_copy.append(line)
    return list_copy


def read_recipe_file(list_copy):
  recipe_file = {}
  items = []
  for i in range(len(list_copy)):
    item = list_copy[i]
    if i == 0:
      items.append(item)
    else:
      if item == "":
        recipe_file[items[0].lower()] = items
        items = []
      elif i == (len(list_copy) - 1):
        items.append(item)
        recipe_file[items[0].lower()] = items
      else:
        items.append(item)

  return recipe_file

def search_by_name(filename: str, word: str):
  list_copy = copy_file(filename)
  recipes = read_recipe_file(list_copy)
  found_name = []
  for dish_name, recipe in recipes.items():
    if dish_name.find(word) != -1:
      found_name.append(recipe[0])
  return found_name

def search_by_time(filename: str, prep_time: int):
  list_copy = copy_file(filename)
  recipes = read_recipe_file(list_copy)
  found_time = []
  for dish_name, recipe in recipes.items():
    time = int(recipe[1])
    name = recipe[0]
    if time <= prep_time:
      found_time.append(name + ", preparation time " + str(time) + " min")
  return found_time




def search_by_ingredient(filename: str, ingredient: str):
  list_copy = copy_file(filename)
  recipes = read_recipe_file(list_copy)
  found_ingredient = []
  for dish_name, recipe in recipes.items():
    time = int(recipe[1])
    name = recipe[0]
    for item in recipe[2:]:
      if item == ingredient:
        found_ingredient.append(name + ", preparation time " + str(time) + " min")
        continue
  return found_ingredient






if __name__ == "__main__":
  # found_recipes_name = search_by_name("recipes1.txt", "cake")
  # for recipe in found_recipes_name:
  #   print(recipe)
    
#     # Pancakes
#     # Cake pops

  # found_recipes_time = search_by_time("recipes1.txt", 20)
  # for recipe in found_recipes_time:
  #   print(recipe)
#     # Pancakes, preparation time 15 min

  found_recipes_ingredient = search_by_ingredient("recipes1.txt", "eggs")
  for recipe in found_recipes_ingredient:
    print(recipe)
#     # Pancakes, preparation time 15 min
#     # Meatballs, preparation time 45 min
#     # Cake pops, preparation time 60 min

# {
# 'pancakes': ['Pancakes', '15', 'milk', 'eggs', 'flour', 'sugar', 'salt', 'butter'], 
# 'meatballs': ['Meatballs', '45', 'mince', 'eggs', 'breadcrumbs'], 
# 'tofu rolls': ['Tofu rolls', '30', 'tofu', 'rice', 'water', 'carrot', 'cucumber', 'avocado', 'wasabi'], 
# 'cake pops': ['Cake pops', '60', 'milk', 'bicarbonate', 'eggs', 'salt', 'sugar', 'cardamom', 'butter']}