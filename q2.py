def nun_size(str): ##פונקציה שבודקת אם מספר בין 0 ל 255
    num=int(str)#מבצעת ש נאם יהיה מספר שלם - הפיכת סטרינג ל אינט
    if(num>=0 and num<=255):#האם המספר בין 0 ל 255
        return True
    return False

#בודק את תקינות האייפי - תוכנית
#האייפי צריך להכיל 4 מספרים בין 0-255 מופרדים עם נקודה ושהספרה ההתחלתית לא תהיה 0



def my_is_digits(str): # האם הסטרינג מורכב רק מספרות
    for i in  range(len(str)):#רץ על כל אורך הסטרינג
        if(ord(str[i])<ord('0') or ord(str[i])>ord('9')):# בדיקה האם הספרה
            return False
    return True
def first_zero(str): #פונקציה שבודקת אם האיבר הראשון הוא 0
    if(len(str)==1): #אם האורך של הסטרינג הוא 1 תחזיר שקר
        return False
    if(str[0]=='0'): #האם במיקום ה 0 באמת יש 0
        return True
    return False#לוגיקל אלס
def dots(str):   # פונקציה בודקת אם יש 2 נקודות אחת אחרי השנייה
    for i in range(len(str)-1):#רץ על הסטרינג פחות 1 כי האחרון יבדוק מספר
        if(str[i]=='.' and str[i+1]=='.'):#אם במיקום i יש נקודה וגם במיקום i+1
            return True#יחזיר אמת
    return False#יחזיר שקר
                         
     
def is_legal_ip(str): #פונקציה שבודקת האם האייפי חוקי או לא
    if(dots(str)==True): #במידה ויש נקודה אחת אחרי השנייה
        return False #החזר פולס
    list=str.split('.') #מפצל את המחרוזת לרשימה כשיש . כל פעם שיש נקודה יפצל
    if(len(list)!=4): #האם אורך הרשימה לא שווה ל 4 החזר פולס
        return False
    for i in range(len(list)): #אם כן רוץ על כל הרשימה
        if(my_is_digits(list[i])==False): #האם כל איבר ברשימה מכיל רק ספרות
            return False
        elif (nun_size(list[i])==False): #האם כל איבר ברשימה בין 0 ל 255
            return False
        elif (first_zero(list[i])==True): #האם המספר הראשון באיבר ברשימה מכיל 0
            return False
        
    return True
def main():
        #בדיקות קלטים
 print(is_legal_ip("192.168.1.1"))
 print(is_legal_ip("125.34.251.43"))
 print(is_legal_ip("001.23.45.123"))
 print(is_legal_ip("125.512.100.xy8"))                  
 print(is_legal_ip("125.512.."))
 print(is_legal_ip("192.168.0.1"))



main()
