import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Hello World",
                         font=("Arial", 25, "bold"))
my_label.pack()

window.mainloop()

def print_value(arg="This is the value"):
    print(arg)


print_value("This is custom value")


def add(*args):
    return sum(args)

print(add(1, 5, 7, 87))
