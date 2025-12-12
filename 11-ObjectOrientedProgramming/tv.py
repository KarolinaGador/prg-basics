# tv.py file
# class definition
class TV:
   def __init__(self, is_on, channel_no, set_channel):
      self.is_on = is_on
      self.channel_no = channel_no
      self.set_channel = set_channel
   def turn_off(self):
      return self.is_on == False
   def turn_on(self):
      return self.is_on == True
   def show_status(self):
      if self.is_on == True:
       self.channel_no == 1
       return f'{self.is_on} {self.channel_no}'
      else:
         return f'{self.is_on}'
   def set_channel(new_channel_no):
      
      