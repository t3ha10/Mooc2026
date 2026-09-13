# Write your solution here:
class Series:
  def __init__(self, title: str, seasons: int, genres: list):
    self.title = title
    self.seasons = seasons
    self.genres = genres
    self.ratings = []

  def rate(self, rating: int):
    self.ratings.append(rating)

  def average_ratings(self):
    number_of_ratings = len(self.ratings)
    if number_of_ratings == 0:
      average = 0
    else:
      average = sum(self.ratings) / number_of_ratings
    return average

  def __str__(self):
    number_of_ratings = len(self.ratings)
    if number_of_ratings == 0:
      comment = "no ratings"
    else:
      comment = f"{number_of_ratings} ratings, average {self.average_ratings():.1f} points"

    return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{comment}"

def minimum_grade(rating: float, series_list: list):
  min_grade = []
  for i in series_list:
    if i.average_ratings() >= rating:
      min_grade.append(i)
  return min_grade
def includes_genre(genre: str, series_list: list):
  same_genre = []
  for i in series_list:
    genres = i.genres
    if genre in genres:
      same_genre.append(i)
  return same_genre




if __name__ == "__main__":

  # s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
  # s1.rate(5)

  # s2 = Series("South Park", 24, ["Animation", "Comedy"])
  # s2.rate(3)

  # s3 = Series("Friends", 10, ["Romance", "Comedy"])
  # s3.rate(2)

  # series_list = [s1, s2, s3]

  # print("a minimum grade of 4.5:")
  # for series in minimum_grade(4.5, series_list):
  #   print(series.title)

  # print("genre Comedy:")
  # for series in includes_genre("Comedy", series_list):
  #   print(series.title)

 
  s = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
  s.rate(5)
  s.rate(3)
  s.rate(2)
  print(s)
