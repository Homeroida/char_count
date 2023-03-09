from tkinter import *



def enter():
   test = entry.get()
   canvas.itemconfig(answe_text, text = f'{test} has {len(test)} characters')



#----------------------UI setup----------------------------

window = Tk()
window.title("String Counter")
window.configure(padx=20, pady=10)


canvas = Canvas(width=200, height=200)
answe_text = canvas.create_text(100,130, text ='String Char Length')
canvas.grid(column=1, row=0)


lable_text = Label(text="Enter Text").grid(row=0,column=0)


button_ent = Button(text="OK", command = enter).grid(row=0,column=2)


entry = Entry(window)

entry.grid(row=0, column=1, padx=10)



window.mainloop()