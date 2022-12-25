def The_Most_frequency_ch(string):
    counterofthechars=[0]*26#make a list counter of the chars freq
    string=string.lower()#make string all to be lower chars
    frequencyappearance=[]#make new list of freq
    for i in range(0,len(string)):#runing all the string
        if string[i].isalpha()==True:#if index in string is a char
            counterofthechars[ord(string[i])-97]+=1#add 1 to counter char sum
    maxvalue=max(counterofthechars)#find the most freq char
    if maxvalue==0:#if the maximum = 0
        return -1#get -1 for user to print
    for i in range(0,26):#range over all alphabet showing the frequent
        if counterofthechars[i]==maxvalue:
            frequencyappearance.append(i+97)#add the alphbet in the list
    return chr(min(frequencyappearance))#return the min of freq
            
def main():
    string=str(input("please enter a string:"))#printing for user
    while string!="Quit" and string!="quit":
        x=string#make x to be the string
        s=The_Most_frequency_ch(string)#make s to be the value of the returning function
        print("mode""('",x,"') ""returns: ",s,sep="")#printing for user
        string=str(input("please enter a string:"))#printing for user
    else:
        print("Thank you for exploring strings and complexity")#printing for user by quit
        
main()#calling for main func

