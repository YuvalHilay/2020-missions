import math
def height(v,a,t):#calc height(y) as function of v a and t
    a = deg2rad(a)#replace to radians
    vy= v*math.sin(a)#calc V m/sec in (Y)
    h=vy*t-(g*(t**2))/2
    return h
def horizontal(v,a,t):#calc road(x) as function of v a and t
    a = deg2rad(a)#replace to radians
    vx = (v*math.cos(a))#calc V m/sec in (X)
    s=vx*t
    return s
def deg2rad(a):
    a = math.pi*(a/180)##replace to radians
    return a

v= float(input("Enter speed M/Sec(Between- 0.0-100.0): ")) #take input a integer number Speed M/sec
a= int(input("enter degree(Between - 0-90): "))#take input a float number (degree)
a = deg2rad(a)#replace to radians
t=0.1#first t after 0.1 sec
g=9.81
while((v >= 0 and v <= 100)and(a>0 and a<90)): # speed must be  (0 < v < 100) and degree must be (0<a<90)
    s = horizontal(v, a, t)
    h = height(v,a,t) 
    while(h>0):
        print("Time: %.1f....S = %.2f  H = %.2f"%(t,s,h))
        t+=0.1
        s = horizontal(v, a, t)
        h = height(v,a,t)
    s = horizontal(v, a, t)
    h = height(v,a,t) 
    print("Time: %.1f....S = %.2f  H = %.2f"%(t,s,h))
    print("Fallen !")   
    v= float(input("Enter speed M/Sec(Between- 0.0-100.0): ")) #take input a integer number Speed M/sec
    a= int(input("enter degree(Between - 0-90): "))#take input a float number (degree)
print("erorr")
