"""
תוסיף אם אתה חושב שלא מימשנו את str

אופציה 2 היא בתוכנית הלימודים
השיטה לוקחת שני מספרים ומחזירה זוג מספרים (tuple) המורכב ממנה ושאריתם
#first sol
def int_to_string(i):
    string = ''
    while True:
        i, remainder = divmod(i, 10)
        string = chr(ord('0') + remainder) + string
        if i == 0:
            break
    return string
num1=0
num2=5
print(int_to_string(num1),type(num1))
print(int_to_string(5),type(num2))

#שיטה שלא בטאפל
#המספר + הקוד האסקי של 0 שהוא בעצם נאל יעביר את הנאם לסטרינג
#sol 2
def int_to_string2(num):
 string = chr(ord("0") + num)
 return string

print(int_to_string2(num1),type(num1))
print(int_to_string2(5),type(num2))

"""
#דרך חשיבה
#כל פעם שמזהה שיש אות זה יוסיף את האות לסטרינג החדש
# ויספור את מספר המופעים של האות וכן יוסיף אותו לאחר האות בסטרינג החדש
#כך בלולאה רץ עד לסוף הסטרינג, כל אות שונה שיפגוש הוא הקאונטר של הסאם יפעל וזה יבצע מה שהוסבר כאמור

def strCompress(string): #פונקציה שעבור כל אות תספר את מספר המופעים שהוא מופיע ברצף ותחזיר a2s4g2 דחיסה
    sum=0 #אתחול משתנה ספירת סכום ל 0
    newstr='' #הגדרת סטרינג חדש
    for i in range(len(string)-1): #רץ על כל הסטרינג פחות מיקום אחד 
        sum+=1 #הוספת ערך 1 לספירת הסכום סאם 
        if(string[i]!=string[i+1]): #האם האות ו זו שאחריה שונות אחת מהשנייה
            newstr+=string[i] #העברת האות לסטרינג החדש
            newstr+=str(sum) #- מספר המופעים של האות העברת סאם כמספר למחרוזת החדשה
            sum=0 #איפוס הסכום ל 0
    newstr+=string[i+1] #הוספה לסטרינג החדש את האות האחרונה
    newstr+=str(sum+1) # הוספה ל סטרינג החדש את הסאם האחרון בתור סטרינג
    return newstr 
def strRestored(string): #פונצקיה שתקבל כסטרינג שמורכב מאותיות ואחריו מספרים ותחזיר את הפונקציה הלא דחוסה
    newstr='' #הגדרת סטרינג חדש
    for i in range(1,len(string),2): #רץ על כל המספרים של הסטרינג כמובן שאחרי אות יגיע מספר ולכן הדילוגים ב 2
        for j in range(int(string[i])): #רץ על מספר הפעמים ש האות צריכה להיות
            newstr+=string[i-1] #מוסיף את האות לסטרינג החדש
    return newstr
#בדיקות עבור מצבי קיצון
def main():
    str=input("enter a string please: ")#printing for user to input a string
    while(str.isalpha()==False):#if all the string contains letters האם מכיל רק אותיות
      str=input("enter a string please (chars only): ")#printing for user to input a string
    else:
        print(strCompress(str))## ותתדפיס קרא לפונקציה שתספור את מספר המופעים של האותיות
    str=input("enter a string please: ")#printing for user to input a string    
    while(str.isalpha()== True or str.isdigit() == True):#if the string contains only chars or only digits האם מכיל רק אותיות או רק מספרים
     str=input("enter a string please(after each char type an integer): ")#printing for user to input a string
    else:
     print(strRestored(str))#printing for user the result of the funtion
main()        