"""
x=int(input("Enter number pls \n"))#User entering number
z=input("n") #details for user about char's action
def squr(x,z):
    for i in range(0,x):       
        print(z,end="")
    print()
    for j in range(0,x):
        print(z,end="")
        x=x-1
    print()
squr(x,z)
"""

def triangle(rows,f):# function triangle rows , f are inside inputs
    for i in range(1, rows + 1):#for all of the rows
      for j in range(1, rows-i+2):# rows - 1 rows before
        print(f, end = '')#printing the char with no space
      print()#printing
rows = int(input("Please Enter the Total Number of Rows  : "))#input for user
f=input("Enter Char pls:") #entering char for user
print("********triangle********")
triangle(rows,f)#calling for the function



