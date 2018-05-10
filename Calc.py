from tkinter import *
 
TK = Tk()
tv = StringVar()
Label(TK, textvariable=tv, relief="groove", borderwidth=3, font=("Courier", 20, "bold"), justify=LEFT, width=50, padx=10, pady=20, takefocus=False,).pack()
Entry(TK, textvariable=tv, takefocus=True,).pack()
 #tv.set("123")


TK.title("Калькулятор")
TK.geometry("400x300")

TK.mainloop()