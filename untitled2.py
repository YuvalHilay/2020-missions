
def my_lower(str):#convert string to lower chars
    new_st = ''
    for ch in str:
        if ch >= 'A' and ch <= 'Z':
            new_st += chr(ord(ch) + ord('a') - ord('A'))
        else:
            new_st += ch
    return new_st

def remove_spaces(str):
    str.replace(" ", "")
    return str
def nottypedchar(str):#func find if there is any char in string
    for ch in str:
        if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch<='z'):
            return True#return TRUE - char was typed
    return False#return False- char wasNT typed
def largest_alphabet(a, n) : # Function that return the largest alphabet 
      
    # Initializing max alphabet to 'a' 
    maxr = 'a'#set the maximum for character A
    # Find largest alphabet 
    for i in range(n) :  
      if (a[i] >= 'a' and a[i]<='z'):
        if (a[i] >= maxr): #if there some char bigger than a
            maxr = a[i] #set the char for the new max 
  
    # Returning largest element 
    return maxr

def sm_alphabet(a, n) : 
      
    # Initializing smallest alphabet to 'z' a
    minr = 'z'; 
  
    # Find smallest alphabet 
    for i in range (n) :  
      if (a[i] >= 'a' and a[i]<='z'):
        if (a[i] <= minr): #if there is a char small than the minimum
            minr = a[i] #set the char to be the new minimum
  
    # Returning smallest alphabet 
    return minr
  
# Driver code 
def main():
    # Character array 
    a= input("Enter a string, please: ")#printing for user
    if not(nottypedchar(a)):#if not any char was typed
        print("sry erorr not any char was typed")#printing for user
    else:
     remove_spaces(a)#del all the spaces
     my_lower(a)#set all the string lower chars
      
    # Calculating size of the string 
     size = len(a) #set size to be the len of the string
      
 
     print( "Largest alphabet is : ", largest_alphabet(a, size)) # Calling functions and print returned value
     print( "smallest alphabet is : ", sm_alphabet(a, size)) # Calling functions and print returned value
  
main()
