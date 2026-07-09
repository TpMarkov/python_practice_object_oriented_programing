import tkinter
from gc import disable
from tkinter import *


def convert_values():
    miles = float(input_area.get())
    kilometers = miles * 1.60934

    kilometers_input.delete(0, END)
    kilometers_input.insert(0, str(kilometers))


window = Tk()
window.minsize(400, 300)
window.title("Kilometer Converter")

# Start button
# ⬇ Every time when we create new element - we need to run pack on it !!!

input_area = Entry(width=20)
input_area.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
kilometers_label = Label(text="Is equal to:")
kilometers_label.grid(column=0, row=1)
kilometers_input = Entry(width=20)
kilometers_input.grid(column=1, row=1)
kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=3, row=1)
convert_button = Button(
    window,
    text="Convert",
    command=convert_values
)
convert_button.grid(column=2, row=2)

window.mainloop()

arr_of_numbers = [1, 5, 67, 7, 4, 3]
arr_of_numbers.sort(reverse=True)
print(arr_of_numbers)
