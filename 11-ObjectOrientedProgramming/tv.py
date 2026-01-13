# tv.py
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on == True:
         if self.channel_no<=len(self.channels):
          print(f'The TV is on: {self.is_on}, channel is {self.channel_no} ({self.channels[self.channel_no-1]}), volume is {self.volume}')
         else:
          print(f'The TV is on: {self.is_on}, channel is {self.channel_no}, volume is {self.volume}')
        else:
            print(f'The tv is on: {self.is_on}') 
      
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list): 
        self.channels.append(channels_list)
    def show_channels(self):
        for indx, i in enumerate(self.channels, start=1):
            print(f'{indx}.{i}')  
    def increase_vol(self):
       if self.volume<10:
          self.volume = self.volume +1
       else:
          self.volume = self.volume   
    def decrease_vol(self):
       if self.volume>0:
          self.volume = self.volume -1
       else:
          self.volume = self.volume              

    
               