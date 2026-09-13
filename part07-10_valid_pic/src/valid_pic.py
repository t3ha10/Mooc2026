# Write your solution here
from datetime import datetime
def check_valid_date(date_str):
  date_box = []
  if date_str[-1] == "+":
    date_box.append(date_str[0:2])
    date_box.append(date_str[2:4])
    date_box.append("18" + date_str[4:6])
  elif date_str[-1] == "-":
    date_box.append(date_str[0:2])
    date_box.append(date_str[2:4])
    date_box.append("19" + date_str[4:6])
  elif date_str[-1] == "A":
    date_box.append(date_str[0:2])
    date_box.append(date_str[2:4])
    date_box.append("20" + date_str[4:6])

  day = int(date_box[0])
  month = int(date_box[1])
  year = int(date_box[2])

  try:
    datetime(year, month, day)
    return True
  except ValueError:
    return False



def check_valid_control_character(pic):
  valid_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
  number_text = pic[0:6] + pic[7:10]

  number = int(number_text)

  index_last_character = number % 31
  try: 
    if valid_characters[index_last_character] == pic[-1]:
      return True
  except ValueError:
    return False





def is_it_valid(pic: str):
  if len(pic) != 11:
    return False
  elif check_valid_date(pic[0:7]) and check_valid_control_character(pic):
    return True
  else:
    return False
  



if __name__ == "__main__":
  print(is_it_valid("230827-906F"))
  # print(check_valid_control_character("230827-906F"))

