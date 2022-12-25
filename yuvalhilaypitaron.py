string = input( "Typ in a string: " )
vowels = "a","e","i","o","u" ,"A","E","I","O","U"
indices = ""
c=""
for i in string:
    if i in vowels:
        indices += i
    if i not in vowels:
        c += i
print(c)
print(indices)
print(type(vowels))
