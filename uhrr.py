from math import cos, sin, radians
from tkinter import Tk, Canvas
from time import time, localtime

def stelle_zeiger(sek, min, hour):
    
    alpha = radians((-6 * sek) + 90)   #radians rechnet von Winkelmaß zur Bogenmaß
    xz = cos(alpha)
    yz = sin(alpha)
    xb = (350 * xz) + 400
    yb  = (-350 * yz) + 400
    myCanvas.coords(sekundenzeiger, 400,400,xb, yb)

    alpha = radians((-360//60 *  (min+sek/60)) + 90)   #radians rechnet von Winkelmaß zur Bogenmaß
    xz = cos(alpha)
    yz = sin(alpha)
    xb = (300 * xz) + 400
    yb  = (-300 * yz) + 400
    myCanvas.coords(minutenzeiger, 400,400,xb, yb)
    sek += 1 # nächste Sekunde
    #sek %= 60  # sek = sek % 60 %: Rest bei Division (Modulo)
    if sek >= 60:
        min += 1
        sek = 0

    alpha = radians(-360//12 *  (hour+min/60) + 90)   #radians rechnet von Winkelmaß zur Bogenmaß
    xz = cos(alpha)
    yz = sin(alpha)
    xb = (200 * xz) + 400
    yb  = (-200 * yz) + 400
    myCanvas.coords(stundenzeiger, 400,400,xb, yb)
    if min >= 60:
        hour += 1
        min = 0
    print(hour, min, sek)
    root.after(1000, lambda: stelle_zeiger(sek, min, hour))

root = Tk()
myCanvas = Canvas(root, bg="black", width= 800, height = 800)
uhr = myCanvas.create_oval(50,50,750,750, fill = "white")
myCanvas.pack()

sekundenzeiger = myCanvas.create_line(400,400,750, 400, fill = "blue", width=2)
minutenzeiger = myCanvas.create_line(400,400,700, 400, fill = "red", width=4)
stundenzeiger = myCanvas.create_line(400,400,600, 400, fill = "black", width=8)

punkt= myCanvas.create_oval(395,395,405,405, fill="black")
# drei = myCanvas.create_rectangle(700, 397, 800, 403, fill="black")
# sechs = myCanvas.create_rectangle(397, 700, 403, 800, fill="black")
# neun = myCanvas.create_rectangle(0, 397, 100, 403, fill="black")
# zwölf = myCanvas.create_rectangle(397, 0, 403, 100, fill="black")

for i in range(60):
    alpha = radians(-6 * i + 90)
    xz = cos(alpha) 
    yz = sin(alpha)
    xa = (350 * xz) + 400
    ya = (-350 * yz) + 400
    xi = (320 * xz) + 400
    yi = (-320 * yz) + 400
    
    myCanvas.create_line(xa, ya, xi, yi, fill = "hotpink", width = 2)

for i in range(12):
    alpha = radians(-360//12 * i + 90)
    xz = cos(alpha)
    yz = sin(alpha)
    xa = (350 * xz) + 400
    ya  = (-350 * yz) + 400
    xi = (300 * xz) + 400
    yi = (-300 * yz) + 400
    
    myCanvas.create_line(xa, ya, xi, yi, fill = "green", width = 4)

s = localtime(time())[5]
m = localtime(time())[4]
h = localtime(time())[3]

stelle_zeiger(s, m, h)

root.mainloop()
