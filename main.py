from tkinter import *

def calculate_clicked():
    '''Prints the Kilometer value.'''
    miles = int(input_box.get())
    km = miles * 1.609
    calculated_km_label.config(text= f"{km}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(height=200, width=200)
window.config(padx=20, pady=20)


label1 = Label(text="is equal to")
label1.grid(row=1, column=0)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

calculated_km_label = Label()
calculated_km_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(row=2, column=1)

input_box = Entry(width=8)
input_box.focus()
input_box.grid(row=0, column=1)


window.mainloop()