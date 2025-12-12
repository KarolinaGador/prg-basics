# class definition
class Song:
   def __init__(self, artist, title, album, year):
      self.artist = artist
      self.title =title
      self.album = album
      self.year = year
   def __str__(self):
      return f'{self.artist} {self.title} {self.album} {self.year}'

# object creation
song1 = Song("Ed Sheeran",'Hearts Dont Break Around Here', "Divide", 2017)
song2 = Song('Queen', 'Bohemian', 'A Night at the opera', 1975)

## object usage
print(song1)
print(song2)