num=int(input("Enter number: ")) #take input a integer number
if(num>0 and num<10): #check if the number have one digit
    print("OK")
n=num #save the original number
numlen=0 #define numlen for the len of the number
while(n!=0): #check the numlen
    numlen+=1
    n=n//10
flag=0 #define flag to check the number
k=num #save the original number
for i in range(0,numlen-2,3): #run on the len of the number and check if three nearby digits have diffrent % by 3
    if((k%10)%3 != ((k//10)%10)%3 != ((k//100)%10)%3):
        flag+=1 #
    else:
        print("ERROR")
        break
    k=k//1000
if(flag>0):
    print("OK")