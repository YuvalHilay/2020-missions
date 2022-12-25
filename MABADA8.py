"""
#MABADA 8 
#TARGIL 1
def create_new_list(L,x):#func that move all numbers lower than x to the begining of the list
#other numbers bigger or equal x stay in the place the was.
 newlist=[]#newlist for numbers lower than x
 newlist2=[]#newlist for numbers equal or bigger than x
 u = []#an UNION LIST of newlist + newlist2
 for i in range(len(L)):#for over all the L
        if(L[i]) < x:
         newlist.append(L[i])#adding for newlist the number that lower than x
        else:
         newlist2.append(L[i])#adding for newlist the number that equal or bigger than x
 for i in newlist:#adding to UNION list
            u.append(i)#adding to union
 for i in newlist2:
            u.append(i)#adding to union
 return u #return the union list
n=int(input("Enter num of elements to the LIST: ")) #input number of the elements
def input_list(n):
 L1=[0]*n #create list with input len
 for i in range(n): #run on len and enter elements to list
  L1[i]=int(input("enter element %d:" %i)) 
 return L1#return the LIST L1
def main():
 t=input_list(n)#L1 = t
 print("Original List:",t) #printing the original List
 x= int(input("Pls enter num: \n"))#input x for the create_new_list func
 z= create_new_list(t,x)#make the new list 
 print("New List:",z)#printing the new LIST
if __name__ == "__main__":
    main()

#TARGIL 2
def my_avg(L1,len):#function calc average time of runners
 counter = 0#set count to 0
 avg=0#set average to 0
 for i in range(len):#runing on LIST L1
       counter+= L1[i]#make sum of result
 avg = counter/len#calc the average results
 return avg#return the average

def runners_below(L1,len,avg):#function calc how many results lower the average
    count=0#set counter to 0
    for i in range(len):
        if(L1[i] < avg):#if result < average of results
         count +=1#add 1 to counter
    return count#return the counter
len=int(input("Enter num of runners: ")) #input nuber of the elements
L1=[0]*len #create list with input len
for i in range(len): #run on len and enter elements to list
 L1[i]=float(input("enter time for runner %d:" %i))
avg=my_avg(L1,len)#call for function that get the average of results and set it to "avg"
countbelow = runners_below(L1, len, avg)#call the func that calc the results below average and set it to "countbelow"
print("Time average: %.2f"%avg)#print the average of results
print("The number of runners, running below average time is:",countbelow)#print how many results below the average


"""
#Targil3
def num_len(num): #fun that get number and return the numlen
    numlen=0 #define numlen for save him
    while(num!=0): #calc numlen
        numlen+=1
        num=num//10#remove 1 digit from num
    return numlen#return the len of the num

def how_manyshown(num):#fun that calc how many each number 1-10 shown in num
 countlist=[0]*10
 while num > 0:
    for i in range(10):
         countlist[num%10]+=1#add 1 to count in the place of num%10
         num = num//10#remove 1 digit from num
    return countlist

def howmanyzeros(num):#fun calc how many zeros inside num 
    counterzero=0#set counter to 0
    while num >0:
        if(num%10==0):
         counterzero+=1#add 1 to counter
         num = num//10#remove 1 digit from num
        else:
         num = num//10#remove 1 digit from num
    return counterzero#return the count

def second_max(countlist):#fun that find the maximum shown of number in our num
    if countlist[1] > countlist[2]:#if count of num 1 > count of num 2
        max_1 = countlist[1]#set max to count of num 1
    else:
        max_1 = countlist[2]#set max to count of num 2
    for i in range(3, len(countlist)):
        if countlist[i] > max_1: #if some num > our max
            max_1 = countlist[i] #set new value to max
    return max_1


num=int(input("Enter number pls:"))#input for user
if num < 0:#if num got -
 num=num*-1#set num as +
if num == 0:#if num = 0
 print("you choose the number 0 - its not matter how many zero you type it will be still zero\n0 shown 1 times\n0 is the max shown")
elif howmanyzeros(num)> 0:# if numbers of zero in num bigger than zero
     z= how_manyshown(num)#set z to the list - (get the func how many shown in num)
     x= num_len(num)#set x to the len of num
     print("The Number: 0 shown:",howmanyzeros(num))#printing how many number 0 shown
     for i in range(1,10):
        if(z[i]>0):
         print("The Number:",i,"shown:",z[i])#printing the digit in num and how many shown
     if(second_max(how_manyshown(num)) < howmanyzeros(num)):
      print("0 is the max, and shown:",howmanyzeros(num),"times")#if the 0 is the max show in number
     elif(second_max(how_manyshown(num)) == howmanyzeros(num)):#if both 0 and the max numbers are max show in number
       for j in range(1,10): 
        if(z[j]==second_max(how_manyshown(num))):#if the digit is the max in num
          print("thenumber:",j,"and 0 are the max number shown in num")#printing max values and 0
       print("\nthe times max numbers shown also [0]:",second_max(how_manyshown(num)))#printing max values
     elif(second_max(how_manyshown(num)) > howmanyzeros(num)):   #if max show in number bigger than the zeros in num
      for x in range(1,10): 
       if(z[x]==second_max(how_manyshown(num))): #if the digit is the max in num
          print("thenumber:",x,"is the most frequent digit shown in num") #printing max values
      print("\nthe times max numbers shown:",second_max(how_manyshown(num)))#print the times max numbers shown

      
else: # if how many zeros in number < 0
     z= how_manyshown(num)#set z to the list - (get the func how many shown in num) 
     x= num_len(num)#set x to the len of num
     for i in range(1,10):
       if(z[i]>0):
        print("The Number:",i,"shown:",z[i])#printing the digit in num and how many shown
     for j in range(1,10): 
       if(z[j]==second_max(how_manyshown(num))):
          print("thenumber:",j,"is the most frequent digit shown in num")#printing max values
     print("\nthe times max numbers shown:",second_max(how_manyshown(num)))#print the times max numbers shown