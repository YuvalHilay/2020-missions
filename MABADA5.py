"""
#mabada5
number=int(input("Enter number pls \n"))#User entering number
countmehalekim = 0 #any counter beggining with 0
if(number>0): #if number bigger than 0
 for i in range (1,number):#doing for from 1 to number
    if(number%i == 0):#integer of i
     countmehalekim = countmehalekim +1#adding for counter
     print(i," ",end="")#print the divisors
else: #if number not bigger than 0
 for i in range (number,0): #doing for from number to 0
    if(number%i == 0):#integer of i
     countmehalekim = countmehalekim +1
     print(i*-1," ",end="") #print the divisors 
if(number==1):
 countmehalekim = countmehalekim +1
 print("1")
if(countmehalekim==0):#if counter = 0
 print("infinity")
else:
 print("\nnumber of divisors is: %d"%countmehalekim)#print number of divisors by counting integer
"""

"""
#TARGIL 2
a1=int(input("Enter first element of geometric progression series: \n"))#User entering number \n"))#User entering number
q=float(input("enter common ration as float: \n"))#User entering number as q
n=int(input("enter an integer n: \n"))#User entering number as n
if(q>=0):#geometric up 
 for i in range (0, n):
    print(int(a1*(q**i))," ",end="")#printing the geometric progression series as int
elif(q<0):#geometric down
 for i in range (0, n):
    print(float(a1*(q**i))," ",end="")#printing the geometric progression series as float

"""
str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
#shela 3
while(str1 != 'q' and str1 !='Q'):#if user press Q or q
 str2=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
 if(str1 == 'a' or str1 == 'A'): #if user press a or A
     num1=int(input("\nEnter number pls \n"))#User entering number
     num2=int(input("\nEnter number pls \n"))#User entering number
     avg = (num1+num2)/2#calc avg
     print("\nthe avarage of these 2 numbers is: %.3f avg"%avg)#printing avarage 3 over point
     if(avg%1==0):#calc if avarage is an integer
         print("\nThe avarage is an integer")#printing for integer
     else:
         print("\nThe avarage is not an integer(float number)")#printing for float number
 if(str1 =='*'):#if user press *
        num3=int(input("\nEnter number pls \n"))#User entering number
        num4=int(input("\nEnter number pls \n"))#User entering number
        multiplynumbers = num3*num4
        print("\nthe multiply of these 2 numbers is: %d"%multiplynumbers)
 if(str1 =='m'):#if user press m
        num5=int(input("\nEnter number pls \n"))#User entering number
        num6=int(input("\nEnter number pls \n"))#User entering number
        print(num5) if num5 < num6 else print(num6)
        #print("the Minimum of these 2 numbers is: %d"%minimum)
 if(str1 =='M'):#if user press M
     num7=int(input("\nEnter number pls \n"))#User entering number
     num8=int(input("\nEnter number pls \n"))#User entering number
     print(num7) if num7 > num8 else print(num8)
     #print("the Maximum of these 2 numbers is: %d"%maximum1)
 if(str1 =='^'):#if user press ^
        num9=int(input("\nEnter number pls \n"))#User entering number
        num10=int(input("\nEnter number pls \n"))#User entering number
        if(num9 == 0 and num10 <0):
         print("\nerror haloka be 0")
        else:
         thepower = num9**num10
         print("\nthe power of these 2 numbers is: %d avg"%thepower)
         if(thepower%1==0):
          print("\nmispar shalem")
         else:
          print("\nmispar lo shalem")
 if(str1!='a'and str1!='A'and str1!='*'and str1!='^'and str1!='M'and str1!='m'):#if user press any other char
         print("\nerror")
print("\nfinish")    
             

    

