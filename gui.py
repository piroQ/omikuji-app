import tkinter as tk
import random
root=tk.Tk()
root.title("Omikuji")
root.geometry("320x200")
root.configure(bg="black")
def omikuji():
    a=random.randint(0,99)
    if 0<=a<=4:
        label.configure(text="Daikichi")
    elif 5<=a<=20:       
        label.configure(text="Kichi")
    elif 21<=a<=33:
        label.configure(text="Chukichi")
    elif 34<=a<=45:
        label.configure(text="Shokichi")
    elif 46<=a<=58:
        label.configure(text="Suekichi")
    elif 59<=a<=69:
        label.configure(text="Sueshokichi")
    elif 70<=a<=78:
        label.configure(text="Shokyo")
    elif 79<=a<=86:
        label.configure(text="Chukyo")
    elif 87<=a<=96:
        label.configure(text="Kyo")
    elif 97<=a<=99:
        label.configure(text="Daikyo") 
    else:
        label.configure("Suekichi")
label=tk.Label(bg="black",fg="white",text="")
button=tk.Button(bg="gray",fg="white",text="Push")
button["command"]=omikuji
label.pack()
button.pack() 
tk.mainloop()