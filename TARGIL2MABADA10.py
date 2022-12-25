def my_bigger(str):
    new_st = ''
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            new_st += chr(ord(ch) + ord('A') - ord('a'))
        else:
            new_st += ch
    return new_st


def my_replace(str,sub):
  len_str = len(str)
  len_sub = len(sub)
  newstring=''
  for i in range(len_str - len_sub + 1):
    if str[i : i+len_sub] == sub:
     for i in range(len_sub):
      newstring+= my_bigger(sub[i])
      i+=len(sub)
    else:
      newstring += str[i:len(sub)]
  return newstring
     
def my_replace2(str1,str2):
       if str1.find(str2) != -1:
        str1 == my_bigger(str1)    
       return str1

string="sfasdas"
str2="sfa"
print(string)
print(str2)
print(my_replace(string,str2))

def main():
    string= input("Enter Text, please: ")#printing for user
    str2= input("Enter Text, please: ")#printing for user
    print(my_bigger(string))
    print(my_replace2(string,str2))
    while string != "" or str2 !="":
     string= input("Enter Text, please: ")#printing for user
     str2= input("Enter Text, please: ")#printing for user
     print(my_bigger(string))
     print(my_replace2(string,str2))
    print("null is typed")
main()
