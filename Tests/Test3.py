from tkinter import *

i = Tk()
i.geometry('300x300')
frame1 = Frame(i, bg='blue')
frame1.pack()
label1 = Label(frame1, text='TEXTO')
label1.grid()

i.update()
print(frame1.winfo_width())
print(label1.winfo_width())
print(frame1.winfo_geometry())

i.mainloop()

ENTENDER PORQUE O UPDATE ATUALIZOU OS DADOS:

https://www.tutorialspoint.com/how-to-get-the-width-of-the-tkinter-widget