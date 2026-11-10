from pyb import Timer, Pin
import time
import tm1637

class Note():
    def __init__(self, hauteur=float(), longueur=int(), nom=str()):
        self.hauteur=hauteur
        self.longueur=longueur
        self.nom=nom
        
    def play(self):
        self.timer = Timer(5, freq=self.hauteur)
        self.channel = self.timer.channel(3, Timer.PWM, pin=Pin('X1'),
        pulse_width_percent=50)
        print(self.timer.freq())
        deadline = time.ticks_add(time.ticks_ms(), self.longueur)
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            pyb.delay(5)
            
    def stop(self):
        self.channel = self.timer.channel(3, Timer.PWM, pin=Pin('X1'),
        pulse_width_percent=0)          
            
display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))

dict_note={"do":Note(262,1000,"do"),"re":Note(293,1000,"re"),"mi":Note(330, 1000, "mi"),}


do=dict_note["do"]
re=dict_note["re"]
mi=dict_note["mi"]

partition=[do, re, mi]

for note in partition:
    print(note.hauteur)
    display.show(note.nom)
    note.play()
    note.stop()


#timer.freq(440)
#timer,freq(mettre la nouvelle fréquence)

#while True:
    
    #timer.freq(528)
    #timer.freq(311.13)
    #timer.freq(528)
    #timer.freq(493.33)
    #timer.freq(293.66)
    #timer.freq(261.63)
