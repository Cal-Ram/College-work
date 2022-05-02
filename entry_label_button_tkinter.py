from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

first_button = Button(window, text="This is the button widget", fg="blue", bg="red")
first_button.place(x=80, y=100)

first_label = Label(window, text="This is the label widget", fg="red", font=("Helvetica", 16))
first_label.place(x=60, y=50)

text_field = Entry(window, text="This is the entry widget", bd=5) # bd is the size of the border, show='*' shows every letter as a star, like a password box
text_field.place(x=60, y=150)


window.title("First Tkinter")
window.geometry("300x200+50+100") # the (+) numbers change where on the screen the window will appear
window.mainloop()


#types of selection widgets can include: radiobutton, checkbutton, combobox, listbox


