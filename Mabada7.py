
def hiovi(num):#fuction calc if num is bigger than 0
 if(num >= 0):
    return True#Make boolian to be True
 else:
    return False#Make boolian to be False

def if2sfarot(num):#function calc if num has 2 digits or more
 if(num >=10):
    return True#Make boolian to be True
 else:
    return False#Make boolian to be False

def LenOfnum(num):#fuction checking the len of the number (how many digits)
  numlen =0
  k = num
  while(k!=0): #check the numlen
   numlen+=1
   k=k//10
  return numlen

def is_inc_ordered(num):
    #answer if all digits in the num are in increase order       
    digit = num % 10
    num = num //10
    while num != 0:
        nextDigit = num % 10
        if nextDigit+1 == digit:
            return False
        digit = nextDigit
        num //= 10
    return True

def is_inc_down(num):
    #answer if all digits in the num are in down order      
    digit = num % 10
    num = num //10
    while num != 0:
        nextDigit = num % 10
        if nextDigit-1 == digit:
            return False
        digit = nextDigit
        num //= 10
    return True

def has_equal_digits(num):#func check if has at least 2 digits same at num
    
    sum=0
    num2=num#gets num2 value to num
    num3=num#gets num3 value to num
    a=num3%10# make a last digit of num3
    numlen = LenOfnum(num)#how many digits num has
    if(numlen >10):#calc if 123456789 is an negetive option
        return False
    while(num3>0):# num 3 >0
        for i in range(numlen):
            if(a==num2%10):
                sum+=1
                num2=num2//10 # get num len 2 less 1 digit from end
            else:
                num2=num2//10# get num len 2 less 1 digit from end
        num2= num
        num3=num3//10
        a=num3%10
    if(sum==numlen):# check the summary if its == numlen
        return True
    return False
    digit = num % 10
    while num >= 10:#num >= 10
        num //= 10
        nextDigit = num % 10#next digit gets the last digit of number
        if digit == nextDigit:#make digit getting value of nextdigit
            return True
    
        digit = nextDigit
        
    return False

num= int(input("Enter Number and i will check if meorbal\n"))
#print(has_equal_digits(num))
#print(is_inc_ordered(num))

if(hiovi(num) == False):#if - before num
 print("your number",num," Is not positive")
elif(if2sfarot(num) == False):#if less than 2 digits 
 print("your number",num,"has to be at least 2 digits to check if Mixed number")
elif(is_inc_ordered(num) == True and is_inc_down(num) == True and has_equal_digits(num) == True):#if mixed number
 print("your number",num," is well - mixed number")
else:#if not 
 print("your number",num," is not well - mixed number") 
