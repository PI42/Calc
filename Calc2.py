from tkinter import *
from tkinter import messagebox
from tkinter import ttk 


root = Tk()
root.title("Калькулятор")
#root.geometry("400x300")

# Кнопки
bttn_list = [
"7", "8", "9", "+", "-",
"4", "5", "6", "*", "/",
"1", "2", "3", "-/+", "=",
"0", ".", "С"
]

r = 1
c = 0

for i in bttn_list:
rel = ""
#cmd = lambda x=i
ttk.Button(root, text=i ).grid(row=r, column=c)
#c += 1
if c>4:
c=0
r += 1


root.mainloop()