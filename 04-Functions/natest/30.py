def f(h, m, format):
    if format=='24':
        return f'{h:02d}:{m:02d}'
    elif format=='12':
        if h<12 and h>0:
          return f'{h:02d}:{m:02d}am'
        elif h==12 and m>1:
           return f'{h:02d}:{m:02d}pm'
        elif h>12 and m>0:
          ha = h-12
          return f'{ha:02d}:{m:02d}pm'
        elif h==12 and m==0:
          return f'{h:02d}:{m:02d}'
        elif h==0:
          return f'12:{m:02d}am'
        
print(f(13, 10, '12'))       
        

        