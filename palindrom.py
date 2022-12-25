def is_palindrom(num):
    rev_num=0
    temp=num
    while (num>0):
        rev_num+=num%10
        num//=10
        if(num==0):
            break
        rev_num*=10
    if (temp==rev_num):
         print("this is a palindrom")
    else:
        print("this is not  a palindrom")

        

is_palindrom(3241123)
is_palindrom(3223)       