from tkinter import *
import functools

class New_Button:
    def __init__(self, using_frame, variable):
        self.button_1 = Button(using_frame, text = 'Button 1',
                               command=functools.partial(self.Func, using_frame))
        self.button_1.pack()
        self.variable = variable  # Save for use in callback.

    def Func(self, to_destroy):
        to_destroy.destroy()
        self.variable.set(True)  # # Change value of the variable.