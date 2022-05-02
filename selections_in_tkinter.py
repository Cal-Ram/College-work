from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
var = StringVar() # Stringvar is used to edit text in tkinter
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)

lb = Listbox(window, height=5, selectmode="multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=180, y=50)

v1 = IntVar()
v2 = IntVar()
c1 = Checkbutton(window, text="Cricket", variable = v1)
c2 = Checkbutton(window, text="Tennis", variable = v2)
c1.place(x=100, y=100)
c2.place(x=180, y=100)

window.title("second tkinter")
window.geometry("400x300+10+10")
window.mainloop()