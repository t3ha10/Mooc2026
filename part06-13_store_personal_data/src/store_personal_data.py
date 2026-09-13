# Write your solution here

def store_personal_data(person: tuple):
  with open("people.csv", "a") as data_file:
    line = f"{person[0]};{person[1]};{person[2]}\n"
    data_file.write(line)

  
if __name__ == "__main__":
  store_personal_data(("Paul Paulson", 37, 175.5))