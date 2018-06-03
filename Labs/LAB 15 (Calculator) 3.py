 # -*- coding: utf-8 -*-
from Tkinter import*
import tkMessageBox
calculator = Tk()
calculator.title('Calculator')
calculator.geometry('246x130')

menubar = Menu(calculator)

def appear(x): 
    return lambda: results.insert(END, x) 

def Zero(): 
    results.insert(END, "0") 
def Refresh():
    results.delete(0, END)
def Equals(): 
    try:
        result = eval(results.get())
    except: 
        result = "Invalid sum" 
    results.delete(0, END) 
    results.insert(0, result)
def Divide2(): 
    try: 
        result = eval(results.get())/2 
    except: 
        result = "Invalid sum" 
    results.delete(0, END) 
    results.insert(0, result)
def Dot():
        results.insert(END, ".")
def sqrt():
    try:
        import math
        result = eval(results.get())
        results.delete(0, END)
        result = float(result)
        result = math.sqrt(result)
        results.insert(0, result)
    except:
        result = 'Invalid Sum'
        results.insert(0, result)

def Plus_Minus():
    try:
        result = eval(results.get())
        results.delete(0, END)
        result = float(result)
        result = -result
        results.insert(0, result)
    except:
        result = 'Invalid Sum'
        results.insert(0, result)
def Bracket_1():
    results.insert(END, "(")
def Bracket_2():
    results.insert(END, ")")
def Times():
    results.insert(END, "*")
def Divide():
    results.insert(END, "/")
def Plus():
    results.insert(END, "+")
def Minus():
    results.insert(END, "-")
def Delete():
    results.delete(-1)
def HYP():
    whiling = True
    Hcalculator = Tk() 
    Hcalculator.title('Hyp Calculator') 
    Hcalculator.geometry('155x120')

    text1 = Frame(Hcalculator, bd=0, width=10, height=10, relief=SUNKEN)
    text1.grid(column=0, row=0, padx=0)
    buttons = Frame(Hcalculator, bd=0, width=5, height=1, relief=GROOVE)
    buttons.grid(column=0, row=1, padx=1)
    
    var = StringVar()
    label1 = Label(text1, textvariable=var, text="Side of the 90 degree angle:")
    label1.pack()
    label1.grid(column=0, row=0)

    numbers1 = StringVar()
    result1 = Entry(text1, textvariable=numbers1, width=15, fg="#003366", bg="#f2f2f2", font="Verdana")
    result1.pack()
    result1.grid(column=0, row=1)

    var2 = StringVar()
    label2 = Label(text1, textvariable=var2, text="Side of the 90 degree angle:")
    label2.pack()
    label2.grid(column=0, row=2)

    numbers2 = StringVar()
    result2 = Entry(text1, textvariable=numbers2, width=15, fg="#003366", bg="#f2f2f2", font="Verdana")
    result2.pack()
    result2.grid(column=0, row=3)

    def Cancel():
        Hcalculator.destroy()
    def Enter():
        import math
        result_1 = 10
        result_2 = 10
        try:
            result_1 = eval(result1.get())
            result_2 = eval(result2.get())
        except:
            tkMessageBox.showerror('Error', 'Sorry but the keywords you entered were incorect')
            result1.delete(0, END)
            result2.delete(0, END)
            Hcalculator.destroy()
            HYP()
        if result_1==0:
            result1.delete(0, END)
            result1.insert(END, 'Number is equal to 0')
        elif result_2==0:
            result2.delete(0, END)
            result2.insert(END, 'Number is equal to 0')
        result = result_1*result_1 + result_2*result_2
        res = math.sqrt(result)
        Hcalculator.destroy()
        results.delete(0, END)
        results.insert(END, res)

    cancel = Button(buttons, bg="White", text="Cancel", width=5, height=1,
    command=Cancel, relief=GROOVE)
    cancel.grid(padx=2, pady=2, column=7, row=0)

    enter = Button(buttons, bg="White", text="Enter", width=5, height=1,     command=Enter, relief=GROOVE)
    enter.grid(padx=2, pady=2, column=8, row=0)

    Hcalculator.mainloop() 
def PI():
    import math
    results.insert(END, math.pi)

screen = Frame(calculator, bd=0, width=500, height=500, relief=SUNKEN)
buttons = Frame(calculator, bd=0, width=5, height=1, relief=GROOVE)
screen.grid(column=0, row=0, padx=0, pady=0)
buttons.grid(column=0, row=1, padx=1) 

numbers = StringVar()
results = Entry(screen, textvariable=numbers, width=24, fg="#003366", bg="#f2f2f2", font="Verdana")
results.pack()
results.grid(column=0, row=0)

numbers=["7", "4", "1", "8", "5", "2", "9", "6", "3"] 

for index in range(9): 
    n=numbers[index] 
    Button(buttons, bg="White", text=n, width=5, height=1, command=appear(n), relief=GROOVE).grid(padx=2, pady=2, row=index%3, column=index/3)

delete= Button(buttons, bg="White", text="←", width=5, height=1, command=Delete, relief=GROOVE) 
delete.grid(padx=2, pady=2, column=3, row=0)

plus_minus= Button(screen, bg="White", text="±", width=5, height=1, command=Plus_Minus, relief=GROOVE) 
plus_minus.grid(padx=0, pady=0, column=1, row=0)
plus_minus.grid_remove()

pi= Button(buttons, bg="White", text="π", width=5, height=1, command=PI, relief=GROOVE) 
pi.grid(padx=0, pady=0, column=5, row=3)
pi.grid_remove()

square_root= Button(buttons, bg="White", text="√", width=5, height=1, command=sqrt, relief=GROOVE)
square_root.grid(padx=2, pady=2, column=5, row=1)
square_root.grid_remove()

hyp= Button(buttons, bg="White", text="hyp", width=5, height=1, command=HYP, relief=GROOVE)
hyp.grid(padx=2, pady=2, column=5, row=0)
hyp.grid_remove()

divide2= Button(buttons, bg="White", text="½", width=5, height=1, command=Divide2, relief=GROOVE)
divide2.grid(padx=2, pady=2, column=5, row=2)
divide2.grid_remove()

times = Button(buttons, bg="White", text="*", width=5, height=1, command=Times, relief=GROOVE) 
times.grid(padx=2, pady=2, column=3, row=1)

divide = Button(buttons, bg="White", text="/", width=5, height=1, command=Divide, relief=GROOVE) 
divide.grid(padx=2, pady=2, column=4, row=1)

plus = Button(buttons, bg="White", text="+", width=5, height=1, command=Plus, relief=GROOVE) 
plus.grid(padx=2, pady=2, column=3, row=2)

minus = Button(buttons, bg="White", text="-", width=5, height=1, command=Minus, relief=GROOVE) 
minus.grid(padx=2, pady=2, column=4, row=2)

bracket_1= Button(buttons, bg="White", text="(", width=5, height=1, command=Bracket_1, relief=GROOVE) 
bracket_1.grid(padx=2, pady=2, column=2, row=3)

bracket_2= Button(buttons, bg="White", text=")", width=5, height=1, command=Bracket_2, relief=GROOVE)
bracket_2.grid(padx=2, pady=2, column=3, row=3)

zero= Button(buttons, bg="White", text="0", width=5, height=1, command=Zero, relief=GROOVE) 
zero.grid(padx=2, pady=2, column=0, row=3)

refresh= Button(buttons, bg="White", text="AC", width=5, height=1, command=Refresh, relief=GROOVE) 
refresh.grid(padx=2, pady=2, column=4, row=0)

dot= Button(buttons, bg="White", text=".", width=5, height=1, command=Dot, relief=GROOVE) 
dot.grid(padx=2, pady=2, column=1, row=3)
 
equals= Button(buttons, bg="White", text="=", width=5, height=1, command=Equals, relief=GROOVE) 
equals.grid(padx=2, pady=2, column=4, row=3)

calculator.config(menu=menubar) #this is used for the menubar
calculator.mainloop()
