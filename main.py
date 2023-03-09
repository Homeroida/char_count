from tkinter import *







def update_label(*args):
   # Get the value of the Entry widget
   string_value = var.get()

   # Get the length of the string
   string_length = len(string_value)

   # Update the label with the length of the string
   label.config(text=f"Dynamic character counter : {string_length}")


def enter():
   string_value = var.get()
   canvas.itemconfig(answe_text,text=f'{string_value} has {len(string_value)}  characters.')


#----------------------UI setup----------------------------

window = Tk()
window.title("String Counter")
window.configure(padx=20, pady=10)

var = StringVar()





canvas = Canvas(width=200, height=200)
answe_text = canvas.create_text(100,130, text ='String Char Length')

canvas.grid(column=1, row=0)


lable_text = Label(text="Enter Text").grid(row=0,column=0)


label = Label(window, text="Dynamic character counter : 0")
label.place(x=90,y=40)

button_ent = Button(text="OK", command = enter).grid(row=0,column=2)


entry = Entry(window,textvariable=var)

entry.grid(row=0, column=1, padx=10)

var.trace("w", update_label)

window.mainloop()