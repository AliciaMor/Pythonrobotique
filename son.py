from pyb import Timer, Pin
import time

class Note():
    def __init__(self):
        self.hauteur=int()
        self.longueur=float()

        
    def play(self):
        self.timer = Timer(5, freq=self.hauteur)
        self.channel = self.timer.channel(3, Timer.PWM, pin=Pin('X1'),
        pulse_width_percent=100)
        print(self.timer.freq())
        deadline = time.ticks_add(time.ticks_ms(), self.longueur)
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            pyb.delay(5)
            
            

do=Note()
do.hauteur=100
do.longueur=1000

re=Note()
re.hauteur=500
re.longueur=1000

mi=Note()
mi.hauteur=1000
mi.longueur=1000

partition=[do,re,mi]

for note in partition:
    print(note.hauteur)
    note.play()

#timer.freq(440)
#timer,freq(mettre la nouvelle fréquence)

#while True:
    
    #timer.freq(528)
    #timer.freq(311.13)
    #timer.freq(528)
    #timer.freq(493.33)
    #timer.freq(293.66)
    #timer.freq(261.63)
