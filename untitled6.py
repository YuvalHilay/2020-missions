def my_replace(s1,sub):
   s1low=s1.lower()
   sublow=sub.lower()
   newrep=''
   for i in range(len(s1)-len(sub)+2):
        if(s1low[i:i+len(sublow)]==sublow):
            newrep+=sublow.upper()
            i+=len(sublow)+1
            
        
        else:
         
            newrep+=s1[i]
            
            
   return newrep    
def main():
    s1= "In this Question we exercise            strings."
    sub= "is"
    print(my_replace(s1,sub))
    
main()