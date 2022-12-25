#Targil 1
weight=int(input("enter weight (in Kg)\n"))#Number of weight user type
height=int(input("the height on Cm\n"))#Number of height user type in cm
height2=float(height/100)#calc height in meters
bmi = float(weight/height2**2)#calc bmi
if bmi < 18.5: #tnai 1
 print("\nUnderWeight")#pelet shel if
if bmi >= 18.5 and bmi < 25:#tnai 2
 print("\nNormal weight")#pelet shel if
if bmi >= 25 and bmi < 30:#tnai 3
 print("\nIncreased weight")#pelet shel if
if bmi >= 30 and bmi < 40 :#tnai 4
 print("\nObese") #pelet shel if
if bmi >= 40:#tnai 5
 print("\nVery high Obese")#pelet shel if
#targil2
Number=int(input("Enter Num with 4 digits\n"))#Enter Number for the user
alafim = int(Number%10)#calc digit number 4 in Number
asarot = int(Number//100%10)#calc digit number 2 in Number
meot = int(Number//10%10)#calc digit number 3 in Number
ahadot = int(Number//1000)#calc digit number 1 in Number
bool2=0#boolian calc if deacreasing or increasing or both
x=0#distance
y=0#distance
z=0#distance
t=0#distance
if Number < 0:#if number lower than 0
  print("\n%d is a negative number. bye bye."%Number)#bye for the user
elif(Number >= 1000 and Number <= 9999):
  print(ahadot,asarot,meot,alafim)
  x=asarot-ahadot#calc distance up arithmetic
  y=alafim-meot#calc distance up arithmetic
  z=ahadot-asarot#calc distance down arithmetic
  t=meot-alafim#calc distance down arithmetic
  if(alafim > meot and meot > asarot and asarot > ahadot and ahadot<alafim and x==y):#calc if increase arithmetic with distance to up
   print("\n%d is increase arithmetic with distance to up "%Number)
   bool2=1
  elif(alafim > meot and meot > asarot and asarot > ahadot and ahadot<alafim and x!=y):#calc if increase aritmatic
   print("\n%d is increase arithmetic"%Number)
   bool2=1
  elif(alafim < meot and meot < asarot and asarot < ahadot and ahadot > alafim and t==z):#calc if decreasing arithmetic with distance to down
   print("\n%d is decreasing arithmetic with distance to down "%Number)
   bool2=1
  elif(alafim < meot and meot < asarot and asarot < ahadot and ahadot > alafim and x != z):#calc if decreasing arithmetic 
   print("\n%d is decreasing arithmetic "%Number)
   bool2=1
  elif(alafim == meot and meot == asarot and asarot == ahadot and ahadot == alafim):#calc if digits are the same like (1111)
   print("\n%d - all digits are the same !"%Number)
   bool2=0
else:
   print("%d is not a 4-digits number. bye bye"%Number)
if bool2==0:#boolian check
    print("\nNon Decreasing and non increasing")
#targil3
children=int(input("enter number of children\n")) #Number of children user type
salary=int(input("enter your monthly salary\n")) #Number of salary user type
military=input("Military service ?\nFor YES enter 'y', otherwise any other character: n\n") #Military User's anwser
valuec = 0 #mishtane shenoad levdok approved
if(military >= 'a' and military <= 'z' or military >= 'A' and military <= 'Z' and salary >= 0 and children >= 0):
 if(military == 'y' and salary >= 5000 and salary <=7500):# tnai 1 la 20%
  print("The mortgage is approved at amount of:",(20/100)*salary)#Mortgage print
  valuec=1# approved = 1
 if((military == 'y' or military == 'n') and salary >= 4000 and salary < 5000 and children >= 4):#2 tnai 2 la 20 %
  print("The mortgage is approved at amount of:",(20/100)*salary)#Mortgage print
  valuec=1# approved = 1
 if(military == 'y' or military == 'n') and (salary > 7500):
  print("The mortgage is approved at amount of:",(30/100)*salary)#Mortgage print
  valuec=1# approved = 1
  
else:
  print("erorr")#if not char and salary not int and children not int
if valuec == 0:#not approved =1
    print("The Mortgage is not approved") #not approved print
