from tkinter import *
import Test2

class Program:
    def __init__(self, root):
        root.geometry('200x200')
        self.main_frame = Frame(root)
        self.main_frame.pack()

        self.notice_lbl = Label(root, text='')
        self.notice_lbl.pack(side=BOTTOM)

        self.hipotetic_variable = BooleanVar(value=False)
        # Set up a trace "write" callback for whenever its contents are changed.
        self.hipotetic_variable.trace('w', self.check_hipotetic_variable)

        self.branch = Test2.New_Button(self.main_frame, self.hipotetic_variable)

        root.mainloop()

    def check_hipotetic_variable(self, *args):
        """Display value of the hipotetic variable."""
        value = self.hipotetic_variable.get()
        self.notice_lbl.config(text=f'hipotetic variable is: {value}')


app = Program(Tk())