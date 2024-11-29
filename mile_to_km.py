from tkinter import *


def button_clicked():
    miles = input.get()
    km = int(miles) * 1.609
    label4.config(text=f"{km}")


window = Tk()
window.title("MILE TO KM CONVERTOR")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

label1 = Label(text="Miles", font=("Arial", 12))
label1.grid(column=2, row=0)
label1.config(padx=10, pady=10)

label2 = Label(text="Km", font=("Arial", 12))
label2.grid(column=2, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text="is equal to", font=("Arial", 12))
label3.grid(column=0, row=1)
label3.config(padx=10, pady=10)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

label4 = Label(text="", font=("Arial", 12))
label4.grid(column=1, row=1)
label4.config(padx=10, pady=10)

window.mainloop()
