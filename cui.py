import random
a=random.randint(0,99)
if 0<=a<=4:
    print("Daikichi")
elif 5<=a<=20       :
    print("Kichi")
elif 21<=a<=33:
    print("Chukichi")
elif 34<=a<=45:
    print("Shokichi")
elif 46<=a<=58:
    print("Suekichi")
elif 59<=a<=69:
    print("Sueshokichi")
elif 70<=a<=78:
    print("Shokyo")
elif 79<=a<=86:
    print("Chukyo")
elif 87<=a<=96:
    print("Kyo")
elif 97<=a<=99:
    print("Daikyo") 
else:
    print("Suekichi")