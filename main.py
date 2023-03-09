from tkinter import *





def enter(*args):
   # test = entry.get()
   canvas.itemconfig(answe_text, text = f'{var.get()} has {len(var.get())} characters')



#----------------------UI setup----------------------------

window = Tk()
window.title("String Counter")
window.configure(padx=20, pady=10)


canvas = Canvas(width=200, height=200)
answe_text = canvas.create_text(100,130, text ='00')
canvas.grid(column=1, row=0)
var = StringVar()

lable_text = Label(text="Enter Text").grid(row=0,column=0)


# button_ent = Button(text="OK", command = enter).grid(row=0,column=2)


entry = Entry(window)

entry.grid(row=0, column=1, padx=10)


var.trace('w', enter)
window.mainloop()
