# tv_show.py
import tv

def main():
    telew = tv.TV()   
    telew.turn_on() 
    telew.set_channel(6)  
    telew.show_status()  

if __name__ == "__main__":
    main()