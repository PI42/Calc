from tkinter import *

AAA = int()
BBB = int()
TK = Tk()
tv = StringVar()
Rezult = int()
RezultView = StringVar()


Label(text="A", padx="15", pady="6", font="15").pack()
Entry(TK, takefocus=True,).pack()
Label(text="B", padx="15", pady="6", font="15").pack()
Entry(TK, takefocus=True,).pack()


tv.set("=")

Label(TK, textvariable=tv, relief="groove", borderwidth=0, font=("Courier", 20, "bold"), justify=LEFT, width=30, padx=10, pady=10, takefocus=False,).pack()
LabelRezult = Label(TK, textvariable=RezultView, relief="groove", borderwidth=2, font=("Courier", 20, "bold"), justify=LEFT, width=30, padx=10, pady=10, takefocus=False,)
LabelRezult.pack()

BtnPlus = Button(text="+", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
BtnPlus.pack(side=LEFT, fill=NONE)
BtnMinus = Button(text="-", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
BtnMinus.pack(side=LEFT, fill=NONE)
BtnUmnoz = Button(text="*", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
BtnUmnoz.pack(side=LEFT, fill=NONE)
BtnRazdel = Button(text="/", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
BtnRazdel.pack(side=LEFT, fill=NONE)


TK.title("Калькулятор")
TK.geometry("400x300")
TK.mainloop()