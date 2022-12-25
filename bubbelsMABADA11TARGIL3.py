def max_sort(n):
    i=len(n)-1
    while i!=0:
        mostbig=i#biggest is the i
        for j in range(0,i):#runing until i - sort limit(O(i))
            if n[mostbig]<n[j]:
                mostbig=j#make j to be biggest
        x=n[mostbig]#make value for x to be the index mostbig
        n[mostbig]=n[i]
        n[i]=x
        i-=1#less 1 to index
    return n
def main():
    list1=[]#create new list and make it to null
    n=int(input("please enter the number of elements in the list:"))#printing for user
    while n!=0:#if 0 found
        for i in range(n):#runing for range n
            num=int(input("enter number:"))#printing for user
            list1.append(num)#add to list
        print("the list,before sorting:",list1)#printing for user
        print("the list,after sorting:",max_sort(list1))#printing for user
        n=int(input("please enter the number of elements in the list:"))#printing for user
        list1=[]#make list to null
    print("thank you for exploring max sort")#printing for user
main()
