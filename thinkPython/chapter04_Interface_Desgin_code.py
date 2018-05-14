import turtle
import math

bob = turtle.Turtle()

#draw right angle
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)

#draw a squre
#for i in range(4):
#   bob.fd(100)
#   bob.lt(90)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

#square(bob, 600)

def polygon(t, length, sides=4):
    for i in range(sides):
        t.fd(length)
        t.lt(360/sides)
    turtle.mainloop()

#polygon(bob, 100, 8)

def circle(t, r):
    cir = 2 * math.pi * r
    return polygon(t, cir, sides=100)

#circle(bob, 1)

def arc(t,r,angle):
    arc_length = (2 * math.pi * r *angle) / 360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle)/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    turtle.mainloop()

#arc(bob,45,200)

#use refactoring

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.fd(angle)

def polygon(t,n,length):
    angle = 360.0/n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length = (2 * math.pi * r * angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n,step_length,step_angle)

def circle(t,r)
    arc(t,r,360)

