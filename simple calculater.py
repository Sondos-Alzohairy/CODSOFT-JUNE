from tkinter import *                                # tkinter module to build GUI

def button_click(number) :                 # handle button clicks and concatenate num [ display 567 not 5 6 7 or 5 ]
    current = entry_box.get()              #  store the existing content before appending the number
    entry_box.delete(0, END)
    entry_box.insert(END, str(current)+ str(number))  # insert the updated num and concatenate by making all var strings

def button_clear():                          #    Clears the content in the entry box.
    entry_box.delete(0, END)

def button_equal():
    #     Evaluates the expression in the entry box and inserts the result into the entry box.
    expression = entry_box.get()
    result = eval(expression)
    entry_box.delete(0, END)
    entry_box.insert(END, result)


gui = Tk()                                           # create object from  tkinter library to use it(use GUI)
gui.title("Simple Calculater")                       # set the title to "Simple Calculater"
gui.geometry('280x300')                              # set the width to 280 pixels and height to 300 pixels
titleLabel = Label(gui, text="Simple Calculater", fg="red", font=(" Courier 20 bold"))
""" create instance from Lable class ( which build text in GUI) to create the txt "Simple Calculater" with red color
    and the font "century" with a size of 20 and bold weight ')'"""

titleLabel.grid(columnspan=4, pady=20)  # call a grid method to span across 4 columns in the grid layout and create empty space

entry_box = Entry(gui)
entry_box.grid(columnspan=4, pady=15, ipadx=70)

btn1 = Button(gui, text='1', height=1, width=7, command=lambda: button_click(1))
btn1.grid(row=2 , column=0 )
btn2 = Button(gui, text='2' , height=1 , width=7, command=lambda: button_click(2))
btn2.grid(row=2 , column=1 )
btn3 = Button(gui, text='3', height=1 , width=7, command=lambda: button_click(3))
btn3.grid(row=2 , column=2 )
btn4 = Button(gui, text='4', height=1 , width=7, command=lambda: button_click(4))
btn4.grid(row=3, column=0 )
btn5 = Button(gui, text='5', height=1 , width=7, command=lambda: button_click(5))
btn5.grid(row=3 , column=1 )
btn6 = Button(gui, text='6', height=1 , width=7, command=lambda: button_click(6))
btn6.grid(row=3 , column=2 )
btn7 = Button(gui, text='7', height=1 , width=7, command=lambda: button_click(7))
btn7.grid(row=4 , column=0 )
btn8 = Button(gui, text='8', height=1 , width=7, command=lambda: button_click(8))
btn8.grid(row=4 , column=1 )
btn9= Button(gui, text='9', height=1 , width=7, command=lambda: button_click(9))
btn9.grid(row=4 , column=2 )
btn0 = Button(gui, text='0', height=1 , width=7, command=lambda: button_click(0))
btn0.grid(row=5, column=0)

btnDot = Button(gui, text='.' , height=1 , width=7, command=lambda: button_click('.'))
btnDot.grid(row= 5, column=1)
btnEqual= Button(gui, text='=' , height=1 , width=7, command=button_equal)
btnEqual.grid(row=5, column=2)
btnClear = Button(gui, text='c', height=1 , width=7, command=button_clear)
btnClear.grid(row=6, column=0)

btnPlus = Button(gui, text='+' , height=1 , width=7, command=lambda: button_click(' + '))
btnPlus.grid(row=2 , column=3 )
btnMins = Button(gui, text='-', height=1 , width=7, command=lambda: button_click(' _ '))
btnMins.grid(row=3 , column=3 )
btnMul = Button(gui, text='*', height=1 , width=7, command=lambda: button_click(' * '))
btnMul.grid(row=4 , column=3 )
btnDiv = Button(gui, text='/', height=1 , width=7, command=lambda: button_click(' / '))
btnDiv.grid(row=5, column=3)









gui.mainloop()

