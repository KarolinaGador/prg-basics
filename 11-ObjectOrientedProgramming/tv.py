# tv.py file
# class definition
class TV:
   def __init__(self, is_on):
      self.is_on = is_on
   def turn_off(self):
      return self.is_on == False
   def turn_on(self):
      return self.is_on == True
   def show_status(self):
      return f'{self.is_on}'