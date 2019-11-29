from Tkinter import *
import time
import datetime
import math

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

class clock(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=200, height=200)
        self.canvas.pack()
        self.face = self.canvas.create_circle(100, 100, 90, fill="white", outline="#DDD", width=1)
        self.draw_marker()
        self.hand_hour =  self.canvas.create_line(100,100,100,30,width=4)
        self.hand_minute =  self.canvas.create_line(100,100,100,30,width=2)
        self.hand_second =  self.canvas.create_line(100,100,100,30,width=1)
        self.canvas.pack()
        self.root.after(0,self.animation)
        self.root.mainloop()

    def draw_marker(self):
        pik = (15 * 1000000)
        for i in range(0, 12):
            s = i * 5 * 1000000
            rs = s % (15 * 1000000) 
            r1 = 90
            r2 = 80
            
            rad = rs*math.pi/(30* 1000000)
            asd1 = r1*r1/(math.tan(rad)*math.tan(rad)+1)
            asd2 = r2*r2/(math.tan(rad)*math.tan(rad)+1)
            x1 = math.sqrt(asd1)
            y1 = math.sqrt(r1*r1-asd1)
            x2 = math.sqrt(asd2)
            y2 = math.sqrt(r2*r2-asd2)
            if s >= 0 and s < pik :
                x1, y1 =100+y1, 100-x1
                x2, y2 =100+y2, 100-x2
            elif s >= pik and s < pik*2 :
                x1, y1 = 100+x1, 100+y1
                x2, y2 = 100+x2, 100+y2
            elif s >= pik*2 and s < pik*3 :
                x1, y1 = 100-y1, 100+x1
                x2, y2 = 100-y2, 100+x2
            else:
                x1, y1 = 100-x1, 100-y1
                x2, y2 = 100-x2, 100-y2
            self.canvas.create_line(x1,y1,x2,y2,width=4, fill="black")
            

    
    def animation(self):
        track = 0
        while True:
            time.sleep(0.025)
            self.update_hands()
            self.canvas.update()
            track = 1

    def update_hands(self):
    	self.canvas.delete(self.hand_second)
        self.hand_second = self.get_second_hand()
        self.canvas.delete(self.hand_minute)
        self.hand_minute = self.get_minute_hand()
        self.canvas.delete(self.hand_hour)
        self.hand_hour = self.get_hour_hand()
    	

    def get_hand(self, s, r, rad, pik, w, f):
        asd = r*r/(math.tan(rad)*math.tan(rad)+1)
        x = math.sqrt(asd)
        y = math.sqrt(r*r-asd)
        if s >= 0 and s < pik :
            x, y =100+y, 100-x
        elif s >= pik and s < pik*2 :
            x, y = 100+x, 100+y
        elif s >= pik*2 and s < pik*3 :
            x, y = 100-y, 100+x    
        else:
            x, y = 100-x, 100-y
        return self.canvas.create_line(100,100,x,y,width=w, fill=f)

    def get_second_hand(self):
        curr_time = datetime.datetime.now()
        s = curr_time.second * 1000000 + (curr_time.microsecond)
        rs = s % (15 * 1000000) 
        r = 90
        rad = rs*math.pi/(30* 1000000)
        return self.get_hand(s, r, rad, (15 * 1000000) , 1, "black")
        

    def get_minute_hand(self):
        curr_time = datetime.datetime.now()
        s = curr_time.minute * 60 + curr_time.second 
        rs = s % (15 * 60)
        r = 70
        rad = rs*math.pi/(30 * 60)
        return self.get_hand(s, r, rad, (15 * 60) , 2, "black")

    def get_hour_hand(self):
        curr_time = datetime.datetime.now() 
        s = (curr_time.hour % 12) * 60 + curr_time.minute
        rs = s % (3 * 60)
        r = 50
        rad = rs*math.pi/(6 * 60)
        return self.get_hand(s, r, rad, (3 * 60) , 4, "red")

        

c = clock()
        

        
