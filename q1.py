def my_split(str,ch): # פונקציה שמקבלת סטרינג ו אות צאר ומחזירה את ה ליסט מופרדת ב אות הזו
    newlist=[] # הגדרת רשימה חדשה היא הרשימה שתהיה מופרדת
    index=0 #מגדיר אינדקס מאותחל שישמר כל פעם ב מיקום אחרי האות
    for i in range(len(str)): #רץ על כל הסטרינג
        if(str[i]==ch): #אם מוצאים את האות במיקום כלשהו בסטרינג
            newlist.append(str[index:i]) #i הוספה לרשימה החדשה תתחיל באינדקס ותסתיים ב 
            index=i+1 #ידלג לתא הבא) מזיזה את אינדקס אחרי האות שנמצאה
    newlist.append(str[index:]) # הוספת שאר הסטרינג הוספת הסאבסטרינג האחרון
    return newlist #מחזיר את הרשימה החדשה
 
str = "This is an example of how split works" #inputing string for - (str)
print (my_split(str, " ")) #calling for the fucntion my_split with the string, and the char
print (my_split(str, "s")) #calling for the fucntion my_split with the string, and the char
print (my_split(str, "x")) #calling for the fucntion my_split with the string, and the char
print (my_split(str, "y")) #calling for the fucntion my_split with the string, and the char



#פיצול מחרוזות לרשימה לפי מה שבסוגריים
#זה בדיוק כמו המתודה ספליט
#x.split('e')
#עבור Braude College
#['Braud', ' Coll', 'g', '']
#ברגע שמגיע e זה יפריד וחסיר את e מהמילה
#וכך ימשיך למילה הבאה