from tkinter import *


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
    labelX['text'] = ''
    if is_digit(a := entryA.get()) and is_digit(b := entryB.get()) and is_digit(c := entryC.get()) and (float(a) != 0):
        labelAns['text'] = 'Ответ:'
        a = float(a)
        b = float(b)
        c = float(c)
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            labelX['text'] = f'x₁={x1}\nx₂={x2}'
        elif d == 0:
            x = -b / (2*a)
            labelX['text'] = f'{x=}'
        else:
            labelX['text'] = 'Нет корней'
    else:
        labelAns['text'] = 'Ошибка:'
        labelX['text'] = 'Неверные\nданные!'


root = Tk()
root.title('Решение квадратных уравнений')
root.config(bg='white')

# doesn't resize by x, y
root.resizable(False, False)

# main font
font = 'Arial 30 bold'

# monitor's parameters (px)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# root's parameters (px)
rootWidth = 500
rootHeight = 500

# root's coordinates
screenX = int(screenWidth/2 - rootWidth/2)
screenY = int(screenHeight/2 - rootHeight/2)

root.geometry(f'{rootWidth}x{rootHeight}+{screenX}+{screenY}')

#main label
Label(text='ax²+bx+c=0', font=font, bg='white').place(anchor=CENTER, relx=0.5, rely=0.1)

#label a, b, c
labelA = Label(text='a', font=font, bg='white').place(anchor=CENTER, relx=0.1, rely=0.25)
labelB = Label(text='b', font=font, bg='white').place(anchor=CENTER, relx=0.1, rely=0.4)
labelC = Label(text='c', font=font, bg='white').place(anchor=CENTER, relx=0.1, rely=0.55)

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
labelX = Label(text='', font=font, bg='white', justify=LEFT)
labelX.place(anchor=W, relx=0.5, rely=0.4)


root.mainloop()