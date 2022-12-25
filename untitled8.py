#shela 3
str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
if(str1!='a'and str1!='A'and str1!='*'and str1!='^'and str1!='M'and str1!='m'):#if user press any other char
  print("\nerror")   
  str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action          
while(str1 != 'q' and str1 !='Q'):#if user press Q or q
    if(str1 == 'a' or str1 == 'A'): #if user press a or A
     num1=int(input("Enter number pls \n"))#User entering number
     num2=int(input("Enter number pls \n"))#User entering number
     avg = (num1+num2)/2#calc avg
     print("the avarage of these 2 numbers is: %.3f avg"%avg)
     if(avg%1==0):#calc if avg is an int
         print("The avarage is an integer")
     else:
         print("The avarage is not an integer(float number)")
     str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
    elif(str1 =='*'):#if user press *
        num3=int(input("Enter number pls \n"))#User entering number
        num4=int(input("Enter number pls \n"))#User entering number
        multiplynumbers = num3*num4#the multiply of these 2 numbers
        print("the multiply of these 2 numbers is: %d"%multiplynumbers)
        str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
    elif(str1!='a'and str1!='A'and str1!='*'and str1!='^'and str1!='M'and str1!='m'):#if user press any other char
        print("\nerror")   
        str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action 
    elif(str1 =='m'):#if user press m
        num5=int(input("Enter number pls \n"))#User entering number
        num6=int(input("Enter number pls \n"))#User entering number
        print("minimum:",num5) if num5 < num6 else print("minimum:",num6)
        str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
       #print("the Minimum of these 2 numbers is: %d"%minimum)
    elif(str1 =='M'):#if user press M
     num7=int(input("Enter number pls \n"))#User entering number
     num8=int(input("Enter number pls \n"))#User entering number
     print("maximum:",num7) if num7 > num8 else print("maximum:",num8)
     str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
     #print("the Maximum of these 2 numbers is: %d"%maximum1)
    elif(str1 =='^'):#if user press ^
        num9=int(input("Enter number pls \n"))#User entering number
        num10=int(input("Enter number pls \n"))#User entering number
        if(num9 == 0 and num10 < 0):#calc for eror
         print("error haloka be 0") #/0 can be real
         str1=input("Enter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
        else:
         thepower = float(num9**num10)#calc the power with float
         print("the power of these 2 numbers is: %f"%thepower)#view the power
         if(thepower%1==0):#if the power is an integer
          print("\nan integer power")
          str1=input("\nEnter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action
         else:
          print("\nnot an integer power")
          str1=input("\nEnter Char\na or A average\n*    multiply\nm    minimum\nM    maximum\n^    power\nQ or q quit\n") #details for user about char's action

else:#if its q OR Q
 print("\nfinish")    
