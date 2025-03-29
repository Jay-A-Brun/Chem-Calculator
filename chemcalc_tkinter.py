from tkinter import *
import chemcalc
class application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.btns = {}
        for i,v in chemcalc.calcOpt.items():
            self.btns[i] = Button(self, text=i, command=lambda: v(self))
            self.btns[i].grid()
root = Tk()
root.title("Chemistry Regents Calculator")
root.geometry("800x600")
app = application(root)
root.mainloop()