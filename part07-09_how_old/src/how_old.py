# Write your solution here
birth_date = int(input("Day: "))
birth_month = int(input("Month: "))
birth_year = int(input("Year: "))

from datetime import datetime
new_millennium_eve = datetime(1999, 12, 31)
birthday = datetime(birth_year, birth_month, birth_date)

duration = new_millennium_eve - birthday

if birthday < new_millennium_eve:
  print(f"You were {duration.days} days old on the eve of the new millennium.")
else:
  print("You weren't born yet on the eve of the new millennium.")

