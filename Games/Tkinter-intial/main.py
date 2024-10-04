from tkinter import *

def change():
    mile=int(in1.get())
    km = mile *1.60934
    converted.config(text=f"{km}")

window = Tk()
window.title("Miles to Km converter : ")
window.minsize(height=100, width=100)
window.config(padx=10, pady=10)

mile = Label(text="Miles")
mile.grid(column=2, row=0)

in1 = Entry(width=10)
in1.grid(column=1, row=0)

equal = Label(text="Is Equal to :")
equal.grid(column=0, row=1)

converted = Label(text="0")
converted.grid(column=1, row=1)

equal = Label(text="km")
equal.grid(column=2, row=1)

btn = Button(text="Calculate",command=change)
btn.grid(column=1, row=2)

window.mainloop()
