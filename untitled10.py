def main():
    
    string = "Computer Science"#create a string Computer Science
    myarray = ["optic", "nirto","option"] #create a list with the words optic , nirto , option
    print("My String:",string,"\n")
    print(hidden_str(string,myarray))
    
def issubinupperstring(string, old):#func check if there is substring in string in upperlevel
    idx = 0#make an obj be 0 (flag)
    for s in old:
        x = string.find(s, idx)#if substring found in the bigger string make the x to the index that found in string
        if x != -1:#if it found
            idx = x#make idx to be x
        else:
            return False#if is not hidden in upper
    return True#if is hidden in upper
    
def issubireversedstring(string, old):
    zdx = 0#make an obj be 0 (flag)
    string2 = string[::-1]#make a reverese string of "string"
    for t in old:
        j = string2.find(t, zdx)#if substring found in the bigger string make the t to the index that found in string
        if j != -1:#if it found
            zdx = j #make zdx to be j
        else:
            return False#if is not hidden in reversed
    return True#if is hidden in reversed

def hidden_str(string,myarray):#func check if hidden or not - check if issubireversedstring or issubinupperstring fucntions are true
    for i in range(3):
        if (issubireversedstring(string,myarray[i]) or issubinupperstring(string,myarray[i])):
            print(myarray[i],"is hidden in",string)
        else:
            print(myarray[i],"is not hidden in",string)
    return("")
            
main()
