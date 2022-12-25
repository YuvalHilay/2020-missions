
#q1
def my_split(str,ch): #fun get str and ch and return list of the str seprate by the ch 
    newlist=[] #define list for the sepreated str
    index=0 #define index for save every time the place after the ch
    for i in range(len(str)): #run on str len
        if(str[i]==ch): #if we find ch in the str
            newlist.append(str[index:i]) #add the newlist the suit substring
            index=i+1 #move index for the index after the ch
    newlist.append(str[index:]) #add the last substring
    return newlist #return our newlist
            
str = "This is an example of how split works" #inputing string for - (str)
print (my_split(str, " ")) #calling for the fucntion my_split with the string, and the char
print (my_split(str, "s")) #calling for the fucntion my_split with the string, and the char
print (my_split(str, "x")) #calling for the fucntion my_split with the string, and the char
print (my_split(str, "y")) #calling for the fucntion my_split with the string, and the char
#more checks
"""
str2= "This is an example of how split works"
print(str2.split('e'))
print (my_split(str, "e"))
print(str2.split('      '))
print (my_split(str, "      "))
print(str2.split('a'))
print (my_split(str, "a"))
#
"""

#q2
def nun_size(str): #funtion check that the number is 0-255
    num=int(str)
    if(num>=0 and num<=255):#check if number between 0 - 255
        return True
    return False
def my_is_digits(str): #function that check the organ have only numbers
    for i in  range(len(str)):
        if(ord(str[i])<ord('0') or ord(str[i])>ord('9')):
            return False
    return True
def first_zero(str): #funtion that check the first digit in the organ isnt zero
    if(len(str)==1): #if the len is one it ok and return false
        return False
    if(str[0]=='0'): #check the first digit in the organ is zero
        return True
    return False
def dots(str):   #funtion check if the ip has two dots next to each other
    for i in range(len(str)-1):
        if(str[i]=='.' and str[i+1]=='.'):
            return True
    return False
                         
     
def is_legal_ip(str): #main fun that get ip and check if ip is legal
    if(dots(str)==True): #call dots that check if the ip has two dots next to each other
        return False #if there is return false
    list=str.split('.') #split the ip by dots
    if(len(list)!=4): #check that the len of the list is 4 and if not return false
        return False
    for i in range(len(list)): #run on every organ on the list
        if(my_is_digits(list[i])==False): #call my_is_digits that check that the organ have only numbers
            return False
        elif (nun_size(list[i])==False): #call nun_size and that check that the number is 0-255
            return False
        elif (first_zero(list[i])==True): #call first_zero that check the first digit in the organ isnt zero
            return False
        
    return True
        



print(is_legal_ip("192.168.1.1"))
print(is_legal_ip("125.34.251.43"))
print(is_legal_ip("001.23.45.123"))
print(is_legal_ip("125.512.100.xy8"))                  
print(is_legal_ip("125.512.."))
print(is_legal_ip("192.168.0.1"))
"""
#more checks
print(is_legal_ip("125.212.."))
print(is_legal_ip("125.1.2.4.2.3.4.5"))
print(is_legal_ip("aartast"))
print(is_legal_ip("a.b.c.r"))
print(is_legal_ip("2511.2233.2515.2322"))
print(is_legal_ip("251.233.215.232.424"))
print(is_legal_ip("000.000.000.000"))
print(is_legal_ip("000000000000"))
print(is_legal_ip("@.@.@.@"))
print(is_legal_ip(" . . . "))
print(is_legal_ip(""))
print(is_legal_ip("  /   /   /   "))
print(is_legal_ip("1.1.1.1"))
"""

#q3
def strCompress(string): #function that compress the string
    sum=0 #define sum for count every letter
    newstr='' #define newstr for the compress string
    for i in range(len(string)-1): #run on string len
        sum+=1 #add to sum every time the letter 
        if(string[i]!=string[i+1]): #if the letter and the letter next diffrent
            newstr+=string[i] #add to newstr the letter
            newstr+=str(sum) #add to newstr the sum
            sum=0 #zeroing sum for next letter
    newstr+=string[i+1] #add to newstr the last letter
    newstr+=str(sum+1) #add to newstr the last sum
    return newstr 
def strRestored(string): #fun that Restored the string
    newstr='' #define newstr for the Restored string
    for i in range(1,len(string),2): #run on the numbers in the string
        for j in range(int(string[i])): #run on the number of time the letter need to be
            newstr+=string[i-1] #add the letter to the newstr
    return newstr
def main():
    str=input("enter a string please: ")#printing for user to input a string
    while(str.isalpha()==False):#if all the string contains letters
      str=input("enter a string please (chars only): ")#printing for user to input a string
    else:
        print(strCompress(str))#printing for user the result of the funtion
    str=input("enter a string please: ")#printing for user to input a string    
    while(str.isalpha()== True or str.isdigit() == True):#if the string contains only chars or only digits
     str=input("enter a string please(after each char type an integer): ")#printing for user to input a string
    else:
     print(strRestored(str))#printing for user the result of the funtion
main()
