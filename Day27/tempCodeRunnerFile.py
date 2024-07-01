from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Mile to Km Converter")
window.config(padx=50,pady=50)

# def mile_to_km(value):
#     value = int(value)
#     return value*1.61

# input
mile_input = Entry()
mile_input.grid(column=1, row=0)

# Mile
mile_label = Label(text="Miles",font=("Times New Roman",20,))
mile_label.grid(column=2, row= 0)
mile_label.config(padx=20, pady=20)


# km
km_label =Label(text="Km")
km_label.grid(column=2, row= 1)

# result label
result_label = Label(text="0")


# is_equal
is_equal_label = Label(text="is equal to",font=("Times New Roman",20,))
is_equal_label.grid(column=0, row=2)

# Buttoon

calculate_button = Button(text="Calculate")






window.mainloop()