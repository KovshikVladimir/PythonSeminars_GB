from tkinter import *
from tkinter import messagebox
# from controller import *
import view

window = Tk()
window.geometry('300x300')
window.title('Телефонный спраквочник 2.0')
window.resizable(width=False,height=False)

text = StringVar()

def changetext(): 
    global text
    entertext = text.get()
    # messagebox.showinfo('Result',f'{entertext}')
    lbl2['text'] = entertext
    
lbl2 = Label(window,text='').pack(side=BOTTOM)
lbl = Label(window,text = 'Введите имя').pack()
enter = Entry(window,textvariable=text).pack()
btn = Button(window,text = 'GO',command= changetext).pack()

window.mainloop()