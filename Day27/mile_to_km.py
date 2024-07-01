from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Mile to Km Converter")
window.config(padx=50,pady=50)

def mile_to_km():
    result_label.config(text=f"{round(float(mile_input.get()) * 1.61,2)}")

# input
mile_input = Entry()
mile_input.grid(column=1, row=0)

# Mile
mile_label = Label(text="Miles",font=("Times New Roman",20))
mile_label.grid(column=2, row= 0)
mile_label.config(padx=20, pady=20)


# km
km_label =Label(text="Km",font=("Times New Roman",20))
km_label.grid(column=2, row= 1)

# result label
result_label = Label(text="0",font=("Times New Roman",20))
result_label.grid(column=1, row=1)
result_label.config(padx=20, pady=20)

# is_equal
is_equal_label = Label(text="is equal to",font=("Times New Roman",20))
is_equal_label.grid(column=0, row=2)
is_equal_label.config(padx=20, pady=20)

# Buttoon

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row= 2)






window.mainloop()