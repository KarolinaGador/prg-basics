# tv.py
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on == True:
         print(f'The TV is on: {self.is_on}, channel is {self.channel_no}')
        else:
            print(f'The tv is on: {self.is_on}') 
      
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list): 
        self.channels.append(channels_list)

    
               