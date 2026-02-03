from tkinter import *

window = Tk()
window.title('Adding Numbers')
window.geometry('400x300')

lbl = Label(text='Hi!', fg='white', bg="#F50733")
lbl.pack()

name_lbl = Label(text='Enter your name', bg="#F51707")
name_lbl.pack()
name_entry = Entry()
name_entry.pack()

number1 = Label(text='Enter your first no', bg="#F51707")
number1.pack()
number1_entry = Entry()
number1_entry.pack()

number2 = Label(text='Enter your second no', bg="#F51707")
number2.pack()
number2_entry = Entry()
number2_entry.pack()

text_box = Text(height=6)
text_box.pack()

def Display():
    name = name_entry.get()
    no1 = int(number1_entry.get())
    no2 = int(number2_entry.get())

    text_box.delete(1.0, END)

    greet = "Hello " + name + "\n"
    message = "Welcome to the application\n"
    ans = "Sum = " + str(no1 + no2)

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, ans)

btn = Button(text='Begin', command=Display, height=1, bg='#1261A0', fg='white')
btn.pack()

window.mainloop()
