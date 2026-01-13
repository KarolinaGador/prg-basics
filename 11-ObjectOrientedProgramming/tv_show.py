# tv_show.py
import tv

def main():
    telew = tv.TV()   
    telew.turn_on() 
    telew.set_channel(4)   
    telew.set_channels('TVP1')
    telew.set_channels('TVP2')
    telew.set_channels('TVP3')
    telew.decrease_vol()
    telew.show_status()
    telew.show_channels()


if __name__ == "__main__":
    main()