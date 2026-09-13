# Write your solution here:
class Clock:
  def __init__(self, hours, minutes, seconds):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours

  def tick(self):
    if self.seconds < 59:
      self.seconds += 1
    else:
      if self.minutes < 59:
        self.minutes += 1
        self.seconds = 0
      else:
        if self.hours < 23:
          self.hours += 1
          self.minutes = 0
          self.seconds = 0
        else:
          self.hours = 0
          self.minutes = 0
          self.seconds = 0

  def set(self, hours, minutes):
    self.seconds = 0
    self.minutes = minutes
    self.hours = hours

  # This method returns the state of the object in string format
  def __str__(self):
    return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
   




if __name__ == "__main__":
  clock = Clock(23, 59, 55)
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)

  clock.set(12, 5)
  print(clock)