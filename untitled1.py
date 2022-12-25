#targil1 mabada9

def largest_char(a) : 
      
    # Initializing max alphabet to 'a' 
    maxr = 'a'#set the maximum for character A
    # Find largest alphabet 
    for i in range(len[a]) :  
        if (a[i] > maxr): #if there some char bigger than a
            maxr = a[i] #set the char for the new max 
  
    # Returning largest element 
    return maxr
  
# Function that return the smallest alphabet 
def smallest_char(a) : 
      
    # Initializing smallest alphabet to 'z' 
    minr = 'z'; 
  
    # Find smallest alphabet 
    for i in range(len[a]) :  
        if (a[i] < minr): #if there is a char small than the minimum
            minr = a[i] #set the char to be the new minimum
  
    # Returning smallest alphabet 
    return minr
      
 
#fortargil1

 # Character string 
quote2= input("Enter a string, please: ")#printing for user
   
 # Calculating size of the string 
size = len(quote2) 
   
 # Calling functions and print returned value 
print( "Largest and smallest alphabet is : ", end = "") 
   
print(largest_char(quote2), end = " and ") 
print(smallest_char(quote2)) 