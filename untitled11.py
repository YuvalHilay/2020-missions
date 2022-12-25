# initializing string  
def howmanyin(test_str):
 all_freq = {} 
  
 for i in test_str: 
     if i in all_freq: 
         all_freq[i] += 1
     else: 
       all_freq[i] = 1
  
# printing result  
 print(type(all_freq))
 print ("Count of all is :\n "
                                        +  str(all_freq)) 



def main():
    #fortagril3
   test_str= input("Enter a string, please: ")
   howmanyin(test_str)
main()  
