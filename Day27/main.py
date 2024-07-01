import tkinter

window = tkinter.Tk()


window.title("ANJESH GUI PROGRAMMING")
window.minsize(500,300)
window.config(padx=100,pady=100)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 15, "normal"))
my_label["text"] = "New Text"

my_label.grid(column=0, row=0)

# Button
def button_clicked():
    print("Button Clicked")
    my_label.config(text= input.get())

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=20,pady=20)

#  New Button

new_butten = tkinter.Button(text="new button")
new_butten.grid(column=2, row=0)
new_butten.config(padx=20,pady=20)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=4, row=3)
 


 
window.mainloop() 