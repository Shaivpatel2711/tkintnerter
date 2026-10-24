from tkinter import *
#window = Tk()
#window.title('oawjdoiajoidjaoiwdjoawjdojadjaw')
#window.geometry('400x400')
#window.mainloop()
from datetime import date
root = Tk()
root.title('papera papares a4size nickname')
root.geometry('400x400')
lb1 = Label(text="hey there", fg="white",bg="black", height=1, width = 300)
name_lb1=Label(text="full namesese", bg="blue")
name_entry=Entry()
def display():
    name = name_entry.get()
    global message
    message="welcome to the applicatiouno\n todays date is:"
    greet = "hello"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn=Button(text="begin",command=display,height=1,bg="blue",fg="white")
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()