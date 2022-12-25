def generate_new_organ(num,a): #fun that get number and digit and create new organ
    newnum=a #define newnum for save the new number we make
    par=10 #define par as a parmeter how help calc new num
    numlen= num_len(num) #get the numlen
    for i in range(numlen-1): #run on numlen for create newnum
        newnum=newnum+((num%10)*par)
        par*=10
        num=num//10
    return newnum    

def num_len(num): #fun that get number and return the numlen
    numlen=0 #define numlen for save him
    while(num!=0): #calc numlen
        numlen+=1
        num=num//10
    return numlen

def last_digit(num): #fun that get number and return the left digit in a number
    numlen= num_len(num) #get numlen
    for i in range(numlen-1): #run on numlen for find last digit 
        num=num//10
    return num

def print_list(l,len): #fun that get list and len of the list and print the list
    print("[", end="")
    for j in range(len-1):
        print("%d, " %l[j] ,end="")
    print("%d]" %l[j+1])
   
def create_new_list(l,len): #fun that get list and len of the list and create new list
    first_last_dig= last_digit(l[0]) #save first number last digit
    newlist=[0]*len #define new list with same len
    for i in range(len-1): #run on list len and insert every place the suit number we create
        lastdig= last_digit(l[i+1])
        newlist[i]=generate_new_organ(l[i],lastdig)
    newlist[i+1]= generate_new_organ(l[i+1], first_last_dig) #insret the last number in the new list with the first number last digiy we save before
    return newlist
    



len=int(input("number of elements: ")) #input nuber of the elements
list=[0]*len #create list with input len
for i in range(len): #run on len and enter elements to list
 list[i]=int(input("enter element %d:" %i))
print("Original array:")
print_list(list,len) #print original list
newlist= create_new_list(list,len) # create our left_circular_shift list
print("shifted array:")
print_list(newlist,len) #print the shifted list
new_str="