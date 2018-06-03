 # -*- coding: utf-8 -*-
import tkMessageBox
from Tkinter import*
hesapmakinesi = Tk()
hesapmakinesi.title("Dream & Aim")
hesapmakinesi.geometry('430x380')
menubar = Menu(hesapmakinesi)


def HYP():
    whiling = True
    hesapmakinesi_2 = Tk()
    hesapmakinesi_2.title('My Calculator') 
    hesapmakinesi_2.geometry('155x120')

    text1 = Frame(hesapmakinesi_2, bd=0, width=20, height=20, relief=SUNKEN)
    text1.grid(column=0, row=0, padx=0)
    bns = Frame(hesapmakinesi_2, bd=0, width=10, height=5, relief=GROOVE)
    bns.grid(column=0, row=1, padx=1)
    
    var = StringVar()
    label1 = Label(text1, textvariable=var, text="Side:")
    label1.pack()
    label1.grid(column=0, row=0)

    numbers1 = StringVar()
    outcome1 = Entry(text1, textvariable=numbers1, width=25, fg="GreenYellow", bg="Orchid", font="Consolas")
    outcome1.pack()
    outcome1.grid(column=0, row=1)

    var2 = StringVar()
    label2 = Label(text1, textvariable=var2, text="Side:")
    label2.pack()
    label2.grid(column=0, row=2)

    numbers2 = StringVar()
    outcome2 = Entry(text1, textvariable=numbers2, width=15, fg="GreenYellow", bg="Orchid", font="Consolas")
    outcome2.pack()
    outcome2.grid(column=0, row=3)

    cancel = Button(bns, bg="SkyBlue", text="Cancel", width=5, height=1,
    command=Cancel, relief=GROOVE)
    cancel.grid(padx=2, pady=2, column=7, row=0)

    enter = Button(bns, bg="LawnGreen", text="Enter", width=5, height=1, command=Enter, relief=GROOVE)
    enter.grid(padx=2, pady=2, column=8, row=0)

    calculator2.mainloop()
    
def FirstBracket():
    outcomes.insert(END, "(")
    
def SecondBracket():
    outcomes.insert(END, ")")
    
def Multiply():
    outcomes.insert(END, "*")
    
def Divide():
    outcomes.insert(END, "/")
    
def Plus():
    outcomes.insert(END, "+")
    
def Minus():
    outcomes.insert(END, "-")
    
def Delete():
    outcomes.delete(-1)
    
def PI():
    import math
    outcomes.insert(END, math.pi)
    
def appear(x): 
    return lambda: outcomes.insert(END, x)

def Zero(): 
    outcomes.insert(END, "0")
    
def Refresh():
    outcomes.delete(0, END)
    
def Equals(): 
    outcome = eval(outcomes.get())
    outcomes.delete(0, END) 
    outcomes.insert(0, outcome)
    
def Divide2():
    outcome = eval(routcomes.get())/2
    outcomes.delete(0, END) 
    outcomes.insert(0, outcome)
    
def Dot():
        outcomes.insert(END, ".")
        
def sqrt():
        import math
        outcome = eval(outcomes.get())
        outcomes.delete(0, END)
        outcome = float(outcome)
        outcome = math.sqrt(outcome)
        outcomes.insert(0, outcome)

def PlusandMinus():
        outcome = eval(outcomes.get())
        outcomes.delete(0, END)
        outcome = float(outcome)
        outcome = -outcome
        outcomes.insert(0, outcome)
        
def Cancel():
        hesapmakinesi.destroy()
        
def Enter():
        import math
        outcome_1 = 10
        outcome_2 = 10
        outcome_1 = eval(outcome1.get())
        outcome_2 = eval(outcome2.get())
        if outcome_1==0:
            outcome1.delete(0, END)
            outcome1.insert(END, 'Number is equal to 0')
        elif outcome_2==0:
            outcome2.delete(0, END)
            outcome2.insert(END, 'Number is equal to 0')
        outcome = outcome_1*outcome_1 + outcome_2*outcome_2
        res = math.sqrt(result)
        hesapmakinesi1.destroy()
        outcomes.delete(0, END)
        outcomes.insert(END, res)

screen = Frame(hesapmakinesi, bd=0, width=500, height=500, relief=SUNKEN)
bns = Frame(hesapmakinesi, bd=0, width=5, height=1, relief=GROOVE)
screen.grid(column=0, row=0, padx=0, pady=0)
bns.grid(column=0, row=1, padx=1) 

numbers = StringVar()
outcomes = Entry(screen, textvariable=numbers, width=44, fg="#003366", bg="#f2f2f2", font="Consolas")
outcomes.pack()
outcomes.grid(column=0, row=0)

numbers=["1", "4", "7", "2", "5", "8", "3", "6", "9"]

for i in range(9): 
    n=numbers[i];  
    Button(bns, bg="Aqua", text=n, width=10, height=5, command=appear(n), relief=GROOVE).grid(padx=2, pady=2, row=i%3, column=i/3)

delete=Button(bns, bg="Salmon", text="←", width=10, height=5, command=Delete, relief=GROOVE) 
delete.grid(padx=2, pady=2, column=3, row=0)

plusandminus=Button(screen, bg="Gray", text="±", width=10, height=5, command=PlusandMinus, relief=GROOVE) 
plusandminus.grid(padx=0, pady=0, column=1, row=0)
plusandminus.grid_remove()

pi= Button(bns, bg="Lime", text="π", width=10, height=5, command=PI, relief=GROOVE) 
pi.grid(padx=0, pady=0, column=5, row=3)
pi.grid_remove()

square_root=Button(bns, bg="SpringGreen", text="√", width=10, height=5, command=sqrt, relief=GROOVE)
square_root.grid(padx=2, pady=2, column=5, row=1)
square_root.grid_remove()

hyp=Button(bns, bg="Gold", text="hyp", width=10, height=5, command=HYP, relief=GROOVE)
hyp.grid(padx=2, pady=2, column=5, row=0)
hyp.grid_remove()

divide2=Button(bns, bg="Yellow", text="½", width=10, height=5, command=Divide2, relief=GROOVE)
divide2.grid(padx=2, pady=2, column=5, row=2)
divide2.grid_remove()

multiply=Button(bns, bg="Blue", text="*", width=10, height=5, command=Multiply, relief=GROOVE) 
multiply.grid(padx=2, pady=2, column=3, row=1)

divide=Button(bns, bg="Orange", text="/", width=10, height=5, command=Divide, relief=GROOVE) 
divide.grid(padx=2, pady=2, column=4, row=1)

plus=Button(bns, bg="Pink", text="+", width=10, height=5, command=Plus, relief=GROOVE) 
plus.grid(padx=2, pady=2, column=3, row=2)

minus=Button(bns, bg="Yellow", text="-", width=10, height=5, command=Minus, relief=GROOVE) 
minus.grid(padx=2, pady=2, column=4, row=2)

FirstBracket=Button(bns, bg="Purple", text="(", width=10, height=5, command=FirstBracket, relief=GROOVE) 
FirstBracket.grid(padx=2, pady=2, column=2, row=3)

SecondBracket=Button(bns, bg="Purple", text=")", width=10, height=5, command=SecondBracket, relief=GROOVE)
SecondBracket.grid(padx=2, pady=2, column=3, row=3)

zero=Button(bns, bg="Khaki", text="0", width=10, height=5, command=Zero, relief=GROOVE) 
zero.grid(padx=2, pady=2, column=0, row=3)

refresh=Button(bns, bg="Crimson", text="C", width=10, height=5, command=Refresh, relief=GROOVE) 
refresh.grid(padx=2, pady=2, column=4, row=0)

dot=Button(bns, bg="Violet", text=".", width=10, height=5, command=Dot, relief=GROOVE) 
dot.grid(padx=2, pady=2, column=1, row=3)
 
equals=Button(bns, bg="Green", text="=", width=10, height=5, command=Equals, relief=GROOVE) 
equals.grid(padx=2, pady=2, column=4, row=3)

hesapmakinesi.config(menu=menubar)
hesapmakinesi.mainloop()
