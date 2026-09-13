
def create_list():
  number_list = []
  while True:
    number = int(input("Number: "))
    if number == 0:
      break
    number_list.append(number)
  return number_list

def calculate(name_list):
  amount = 0
  total = 0
  mean = 0
  max_number = None
  min_number = None
  for number in name_list:
    amount += 1
    total += number
    if max_number == None or max_number < number:
      max_number = number
    if min_number == None or min_number > number:
      min_number = number
  
  mean = total / amount
  return amount, total, mean, max_number, min_number

number_list = create_list()
amount, total, mean, max_number, min_number = calculate(number_list)

print(number_list)
print("Lukujen kokonaismäärä: ", amount)
print("Kaikkien numeroiden summa: ", total)
print("Keskiarvo: ", mean)
print("Maksimiarvo: ", max_number)
print("Minimiarvo: ", min_number)



