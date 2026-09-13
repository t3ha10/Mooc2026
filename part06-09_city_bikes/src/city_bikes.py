# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
  stations = {}
  with open(filename) as new_file:
    for line in new_file:
      parts = line.split(";")
      if parts[0] == "Longitude":
        continue
      stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations
  # {
  # "Kaivopuisto": (24.950292890004903, 60.155444793742276),
  # "Laivasillankatu": (24.956347471358754, 60.160959093887129),
  # "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
  # }



def distance(stations: dict, station1: str, station2: str):
  import math
  found_stations = {}
  for station, location in stations.items():
    if len(found_stations) == 2:
      break
    if station == station1 or station == station2:
      found_stations[station] = location

  # we will need the function sqrt from the math module 
  longitude1 = found_stations[station1][0]
  longitude2 = found_stations[station2][0]
  latitude1 = found_stations[station1][1]
  latitude2 = found_stations[station2][1]

  x_km = (longitude1 - longitude2) * 55.26
  y_km = (latitude1 - latitude2) * 111.2
  distance_km = math.sqrt(x_km**2 + y_km**2)
  return distance_km

def greatest_distance(stations: dict):
  greatest = 0
  for station1, location1 in stations.items():
    for station2, location2 in stations.items():
      if station1 == station2:
        continue
      d = distance(stations, station1, station2)
      if d > greatest:
        greatest = d
        s1 = station1
        s2 = station2
  return s1, s2, greatest





  


if __name__ == "__main__":
  stations = get_station_data('stations1.csv')
  d = distance(stations, "Designmuseo", "Hietalahdentori")
  print(d)
  d = distance(stations, "Viiskulma", "Kaivopuisto")
  print(d)

  station1, station2, greatest = greatest_distance(stations)
  print(station1, station2, greatest)
  # Laivasillankatu Hietalahdentori 1.478708873076181


