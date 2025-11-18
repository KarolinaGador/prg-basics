 
def time_string(hours, minutes, time_format):


   if hours < 0 or hours > 23:
        return "error"
   if minutes < 0 or minutes > 59:
        return "error"

   if time_format == '24':
        return f"{hours:02d}:{minutes:02d} "

   elif time_format == '12':
        period = "AM" if hours < 12 else "PM"
           
        display_hours = hours
        if hours == 0:
            display_hours = 12
        elif hours > 12:
            display_hours = hours - 12

        return f"{display_hours:02d}:{minutes:02d}  {period}"

print(time_string(15, 38, '12')) 
print(time_string(12, 00, '12') )
