#targil3
def deltheEnter(quote):#function create space between lines for each space in quote

 for x in quote.split():#spliting - all the words go to some list 
    print(x)#printing the list line after line :)
    
    
#forTargil3
def main():
 quote= input("Enter a string, please: ")#printing for user
 while quote != "":#while not null is typed by the user
  deltheEnter(quote)
  quote= input("Enter a string, please: ")#printing for user
 print("empty string was typed") #printing for user for empty string
 
main()#call for main
