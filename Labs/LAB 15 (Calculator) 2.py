from Tkinter import *

def frame(root, side): 
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None): 
    w = Button(root, text=text, command=command) 
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class SimpleCalculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Verdana 12')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Kurma 1EN04B')
        self.master.iconname("calc1")

        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)

        for key in ("789", "456", "123",  "-0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, c=char: w.set(w.get() + c))

        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                mpn = button(opsF, LEFT, char)
                mpn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                mpn = button(opsF, LEFT, char, lambda w=display, s=' %s '%char: w.set(w.get()+s))

        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    SimpleCalculator().mainloop()
