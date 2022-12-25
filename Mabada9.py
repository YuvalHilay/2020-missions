#MABADA 9

#targil1
def largest_char(a) : 
      
    # Initializing max alphabet to 'a' 
    maxr = 'a'#set the maximum for character A
    # Find largest alphabet 
    for i in range(len(a)) :  
        if (a[i] > maxr): #if there some char bigger than a
            maxr = a[i] #set the char for the new max 
  
    # Returning largest element 
    return maxr
  
# Function that return the smallest alphabet 
def smallest_char(a) : 
      
    # Initializing smallest alphabet to 'z' 
    minr = 'z'; 
  
    # Find smallest alphabet 
    for i in range (len(a)) :  
        if (a[i] < minr): #if there is a char small than the minimum
            minr = a[i] #set the char to be the new minimum
  
    # Returning smallest alphabet 
    return minr
      
          

#targil3
def deltheEnter(quote):#function create space between lines for each space in quote
  start = 0#set start obj to 0
  space_index = quote.find(" ")#find if any space as found
  while space_index != -1:#as find 
     print (quote[start:space_index])
     start = space_index+1
     space_index = quote.find(" ", space_index+1)
  else:
     print (quote[start::1])#make the slicing
     
#targil2
def no_identical_letter_attached(str):
    newstr=''
    last=str[-1]
    for i in range(len(str)-1):
        if(str[i]!=str[i+1]):
            newstr= newstr+str[i]
    newstr=newstr+last

    print("After removing all duplicates:",newstr)

    
def main():
    #fortagril3
   str= input("Enter a string, please: ")#printing for user
   no_identical_letter_attached(str)#send str to function no_identical_letter_attached
   #forTargil2

   quote= input("Enter a string, please: ")#printing for user
   while quote != "":#while not null is typed by the user
    deltheEnter(quote)
    quote= input("Enter a string, please: ")#printing for user
   print("empty string was typed") #printing for user for empty string
   #fortargil1
   
    # Character string 
   quote2= input("Enter a string, please: ")#printing for user
      
    # Calculating size of the string 
   size = len(quote2) 
      
    # Calling functions and print returned value 
   print( "Largest and smallest alphabet is : ", end = "") 
      
   print(largest_char(quote2, size), end = " and ") 
   print(smallest_char(quote2, size)) 
          
    
main()  

""