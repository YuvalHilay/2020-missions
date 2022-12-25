#import math
"""
def box(n,Z): 
    while(n!=1):
     for i in range(n):     
         for j in range(n-1):
             print(Z,end="")
             n-=1

   
Z = input("Enter some Char: ") #take input a integer number
n=int(input("Enter number: ")) #take input a integer number
box(n,Z)


"""
"""
for (int i = 1; i <= 10; ++i)
{
    for (int j = 1; j <= 10; ++j)
    {
        Console.Write(i * j);
        Console.Write(" ");
    }
    Console.WriteLine();
}
"""

def squr(x):
    for i in range(1,x):       
        print('Z',end="")
    print()
    while(x!=1):
     for j in range(x-3):
        print('Z',end="")
        x= x-1
    print()
squr(5)

"""


g=9.81
def height(v,a,t):
    vy= v*math.cos(a)
    h=vy*t-(g**2)/2
    return h
def horizontal(v,a,t):
    vx = v*math.sin(a)
    s=vx*t
    return s
def deg2rad(a):
    radians = a*math.pi(90/180)  
    return radians
             #a*math.pi/180
v=float(input("Enter speed M/Sec(Between- 0.0-100.0): ")) #take input a integer number
a=int(input("enter degree(Between- 0-90): ")) #take input a integer number
if (v <0.0 or v >100.0 or a<0 or a>90):
    print("error")
else:
    while(height
"""