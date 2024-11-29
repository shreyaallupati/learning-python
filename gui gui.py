from tkinter import *


def button_clicked():
    new_text = input.get()
    label.config(text=new_text)


window = Tk()
window.title("gui gui")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# LABEL
label = Label(text="label...", font=("Arial", 24, "bold"))
label.config(text="New text")
label.grid(column=0,row=0)
label.config(padx=10,pady=10)

# BUTTON
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me")
new_button.grid(column=2, row=0)

# entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
