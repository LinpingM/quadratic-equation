from tkinter import *
from math import sqrt


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def click(event):
    labelX1['text'] = ''
    labelX2['text'] = ''
    a = entryA.get()
    b = entryB.get()
    c = entryC.get()
    if is_digit(a) and is_digit(b) and is_digit(c) and float(a) != 0:
        labelAns['text'] = 'Ответ:'
        a = float(a)
        b = float(b)
        c = float(c)
        d = b * b - 4 * a * c
        if d > 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            labelX1['text'] = 'x₁={}'.format(x1)
            labelX2['text'] = 'x₂={}'.format(x2)
        elif d == 0:
            x = -b / (2 * a)
            labelX1['text'] = 'x={}'.format(x)
        else:
            labelX1['text'] = 'Нет корней'
    else:
        labelAns['text'] = 'Ошибка:'
        labelX1['text'] = 'Неверные'
        labelX2['text'] = 'данные!'


root = Tk()

#window's name
root.title('Решение квадратных уравнений')

#backgrond is white
root.config(bg='white')

#not resize
root.resizable(False, False)

#main font
font = 'Arial 30 bold'

#monitor's parameters
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

#window's parameters
rootWidth = 500
rootHeight = 500

#window's coordinates
screenX = int(screenWidth / 2 - rootWidth / 2)
screenY = int(int(screenHeight) / 2 - rootHeight / 2)

root.geometry('{}x{}+{}+{}'.format(rootWidth, rootHeight, screenX, screenY))

#main label
label = Label(text='ax²+bx+c=0', font=font, bg='white')
label.place(anchor=CENTER, relx=0.5, rely=0.1)

#label a, b, c
labelA = Label(text='a', font=font, bg='white')
labelB = Label(text='b', font=font, bg='white')
labelC = Label(text='c', font=font, bg='white')
labelA.place(anchor=CENTER, relx=0.1, rely=0.25)
labelB.place(anchor=CENTER, relx=0.1, rely=0.4)
labelC.place(anchor=CENTER, relx=0.1, rely=0.55)

#entrys a, b, c
bgEntry = '#f0f0f0'
entryA = Entry(bg=bgEntry, font=font, width=4, bd=0, background='#f0f0f0')
entryB = Entry(bg=bgEntry, font=font, width=4, bd=0, background='#f0f0f0')
entryC = Entry(bg=bgEntry, font=font, width=4, bd=0, background='#f0f0f0')
entryA.place(anchor=CENTER, relx=0.3, rely=0.25)
entryB.place(anchor=CENTER, relx=0.3, rely=0.4)
entryC.place(anchor=CENTER, relx=0.3, rely=0.55)

#main batton
button = Button(text='Решить', font=font, bd=0, bg='#f0f0f0')
button.place(anchor=CENTER, relx=0.5, rely=0.8)
button.bind('<Button-1>', click)

#answer label
labelAns = Label(text='Ответ:', font=font, bg='white')
labelAns.place(anchor=W, relx=0.5, rely=0.25)

#x label
labelX1 = Label(text='', font=font, bg='white')
labelX1.place(anchor=W, relx=0.5, rely=0.4)
labelX2 = Label(text='', font=font, bg='white')
labelX2.place(anchor=W, relx=0.5, rely=0.55)


root.mainloop()