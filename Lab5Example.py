# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 07:58:37 2020

@author: Owner
some examples
"""

go=True
i=0

while i<3 and go:
    i=int(input("Enter num: "))
    if i==-10:
        print ("you are 10")
        go=False
    if(go):
        print(":-)")
        if i==2:
            continue;
        print("=:-)")
        
    
print(i)    




i=0

while i<3:
    i=int(input("Enter num: "))
    if i==-10:
        print ("you are 10")
        break;
    print(":-)")
    if i==2:
        continue;
    print("=:-)")
        
    
print(i)    





for i in range (0, 5):
    x=int(input("Enter num: "))
    if x==-10:
        print ("you are 10")
        break;
    print(":-)")
    if x==2:
        continue;
    print("=:-)")
        
    


x='6'
print("A") if x=='a' else print("B")

if x=="a":
    print("A")
else:
    print("B")

Str1="Hello"
for i in Str1:
    print(i)
    

