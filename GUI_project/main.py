import tkinter
from tkinter import *


def click_me():
    if len(input_area.get()) > 0:
        my_label.config(text=input_area.get())
    else:
        my_label.config(text="Please type some text in the input area!")
    input_area.delete(0, END)


window = Tk()
window.minsize(400, 300)
window.title("First GUI Program")
# Label
my_label = Label(text="Hello World",
                 font=("Arial", 25, "bold"))
my_label.config(text="This is my first GUI program")
my_label.pack()

# Start button
start_button = Button(text="Start", command=click_me)
# ⬇ Every time when we create new element - we need to run pack on it !!!
start_button.pack()

input_area = Entry(width=40)

input_area.pack()

window.mainloop()
