# this will be a basic calculator to make sure that I have understood the concepts of tkinter
from tkinter import *

def get_nums():
    a = first_number.get()
    b = second_number.get()
    return [a, b]

def add():
    a = first_number.get()
    b = second_number.get()
    return a + b
    

def subtract():
    a = first_number.get()
    b = second_number.get()
    return a - b

def multiply():
    a = first_number.get()
    b = second_number.get()    
    return a * b


window = Tk()

first_number = Entry(window, text="first number")
first_number.place(x=100, y=50)

second_number = Entry(window, text="second number")
second_number.place(x=150, y=50)

button_add = Button(window, text="add", command=lambda :add)
button_add.place(x=10, y=20)

window.title("hello")
window.geometry("1000x800")
window.mainloop()