from tkinter import *
import view
import logger
# import visual
fil = 'Seminar_8/final_file_new.txt'
def prog_start():
    window = Tk()
    window.geometry('600x400+425+200')
    btn1 = Button(window,text='Import Data', command=importer).grid(row=1,column=1)
    btn1 = Button(window,text='Export Data', command=exporter).grid(row=1,column=2)

    def importer():
        asking = Label(window,text='Введите данные').grid()
        a = view.get_name
        b = view.get_number
        c = view.get_description
        
        global fil
        logger.log(f'Ввели имя: {a}\n Ввели номер телефона: {b}\n Ввели описание: {c}')
        with open(fil, 'a') as f:
            f.writelines(f'{a} - {b} : {c}\n\n')
    
    
    def exporter():
        global fil
        texting = Label(text='Введите необходимые данные').grid(row=2,column=1)
        enter = Entry(textvariable=word)
        word = enter.get()
        with open(fil, 'r') as f:
            readfile = f.readlines()
            for line in readfile:
                if word in line:
                    final_text = Label(text=f'{line}').grid(row=2,column=2)
                else:
                    final_text2 = Label(text=f'{line}').grid(row=2,column=2)
    window.mainloop()

                    
    