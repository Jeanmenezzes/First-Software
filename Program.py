# Commit test

# THIS PROGRAM WILL BE UPLOADED WITH JUST THE FOUR APPS ALREADY SET

# THIS PROGRAM WILL BE UPLOADED WITHOUT BUT IT NEEDS TO HAVE USER'S NAME AND A WELLCOME MESSAGE
# THIS PROGRAM WILL BE UPLOADED WITHOUT BUT IT NEEDS TO HAVE A USER PROFILE SCREEN

# CONTINUE FROM HERE
# UNDERSTAND THE TCLERROR AT LINE 151 WHAT HAPPENS WHEN THE BACK BUTTON RETURNS TO THE CREATE SCREEN
# THE PROBLEM WHAT GENERATES TCLERROR MAY BE THAT WHEN WE GO BACK TO THE CREATE MENU FROM THE LOGIN MENU THE VARIABLE
# variable_profile_name IS REWRITTEN AND CREATE TWO, THREE, FOUR.. VARIABLES EVERY TIME THE BACK BUTTON CALLS THE CREATE
# MENU, MAYBE OVERLOOK THE ARGUMENTS MAY RESOLVE THIS PROBLEM, OTHER SOLUTION IS JUST PUT THE PROFILE FUNCTIONS TOGETHER
# IN THE Program.py FILE.

# 06-03-23
# I ALSO CHECKED THAT WHEN I GOT THE SCREEN OF CREATE USER MENU FOR THE SECOND TIME, AFTER USE THE BACK BUTTON, I GOT
# THE EXCEPTION FROM TKINTER (TCLERROR) BECAUSE THE DATABASE FUNCTION IN THE PROFILE_FUNCTIONS (CREATE) IS CALLED, WHAT
# DOESN'T HAPPEN WHEN IT WAS CALL AT FIRST TIME, BEFORE USE THE BACKBUTTON, I NEED TO CHECK IF I GOT THE SAME ERROR EVEN
# I ACCESS THE CREATE MENU FOR THE FIRST TIME WITHOUT USE BACKBUTTON, OTHERWISE CREATING A NEW PROFILE AND ACCESSING
# TWO TIMES.



# I ALSO SHOULD SEARCH ABOUT Tkinter.TclError IN THE OFFICIAL DOCUMENTATION

# IT'S NEEDED TO  FIX AND MARIO APP
# IT'S NEEDED TO CHANGE TO ENGLISH THE MARIO APP

# CREATE A VIDEO WITH THE EXECUTION OF THE PROGRAM AND UPLOAD THIS IN TO YOUTUBE
# LEARN HOW TO CREATE A EXECUTABLE PROGRAM IN PYTHON

# Importing All Modules
import os
import sys
import pdb
from tkinter import *


# Adding to path files with other functions
sys.path.append('Apps')
sys.path.append('Images')


# The main object Program
class Program(object):
    def __init__(self, root):
        # Parameters to the window
        self.axis_x = 500
        self.axis_y = 500
        self.main_Color = '#c3c3c3'

        # Construction of main screen
        self.root = root
        self.root.geometry('%ix%i' % (self.axis_x, self.axis_y))
        self.root.resizable(0, 0)
        self.root.title('Python - My First Software')
        self.root.wm_iconbitmap('Images/icon.ico')
        self.root['bg'] = self.main_Color
        self.main_Frame = Frame(root, bg=self.main_Color)
        self.main_Frame.pack()

        # This variable contains the function of the last screen used, and may be clicked to back to there
        self.last_screen = None

        # This variable is responsible to activate the back button
        self.variable_arrow = BooleanVar(value=False)
        self.variable_arrow.trace('w', self.set_back_screen)

        # This BooleanVar have the function to call all functions of the profile and login screens
        self.variable_profile = BooleanVar(value=False)
        self.variable_profile.name = 'Any'
        self.variable_profile.trace('w', self.checker_profile_screen)

        # This BooleanVar have the function to call all functions of the apps screens
        self.variable_apps = BooleanVar(value=False)
        self.variable_apps.name = 'Any'
        self.variable_apps.trace('w', self.app_executing)

        # Calling the function what constructs the heading
        self.main_screen()

    # Function that contains the fixed logo, frame with login and create button
    def main_screen(self):
        # Button Responsible to turn back to the previous screen
        from creating_button_function import new_button
        self.back_button = new_button('Images/Arrow.png', self.main_Frame, self.main_Color, self.variable_arrow)
        self.back_button.grid(column=1, row=0, sticky=E)

        self.profile_button = new_button('Images/Profile_shadow.png', self.main_Frame, self.main_Color,
                                         self.variable_profile)
        self.profile_button.grid(column=1, row=1, sticky=E)

        # Part what store the logo and back button
        self.f_logo = PhotoImage(file='Images/main_logo.png')
        self.title = Label(self.main_Frame, image=self.f_logo, bg=self.main_Color)
        self.title.grid(column=0, row=0, rowspan=2, sticky=W)

        self.frame_options = Frame(self.main_Frame, bg=self.main_Color)
        self.frame_options.grid(column=0, row=2, columnspan=2)

        # Importing and execute the login function
        from Profile_Functions import Login
        Login(self.frame_options, self.main_Color, self.variable_profile)

    # This function changes the attribute name of variable_profile to the last screen and calls checker function
    def set_back_screen(self, *args):
        if self.last_screen is not None:
            if self.last_screen == 'login_to_apps':
                self.variable_profile.name = 'Login'
                self.last_screen = 'Apps'
            elif self.last_screen == 'login_to_create':
                self.variable_profile.name = 'Login'
                self.last_screen = 'Create'
            else:
                self.variable_profile.name = self.last_screen

            print(self.main_Frame.grid_slaves())
            self.frame_options.destroy()
            print(self.frame_options)
            self.checker_profile_screen()

    def account_screen(self):
        self.frame_options.destroy()
        self.frame_options = Frame(self.main_Frame, bg=self.main_Color)
        self.frame_options.grid(column=0, row=2, columnspan=2)

    # This function is used to direct the program to the due profile part
    def checker_profile_screen(self, *args):
        # For Apps Screen
        if self.variable_profile.name == 'Apps':
            from creating_button_function import new_button
            self.frame_options = Frame(self.main_Frame, bg=self.main_Color)
            self.frame_options.grid(column=0, row=2, columnspan=2)

            self.buttons_dict = {}
            cont = 0
            for app in os.listdir('Apps'):
                if app == 'To Organize' or app == '__pycache__':
                    continue
                cont += 1
                self.buttons_dict[app] = new_button('Images/%s_ico.png'%app[:-3], self.frame_options, self.main_Color,
                                                    self.variable_apps)
                self.buttons_dict[app].grid(row=(cont-1)//2, column=cont % 2, pady=2)

            self.last_screen = 'login_to_apps'

        # For the create user menu's screen
        elif self.variable_profile.name == 'Create':
            from Profile_Functions import Create
            self.frame_options = Frame(self.main_Frame, bg=self.main_Color)
            self.frame_options.grid(column=0, row=2, columnspan=2)
            Create(self.frame_options, self.main_Color, self.variable_profile)

            self.last_screen = 'login_to_create'

        # For the login screen
        elif self.variable_profile.name == 'Login':
            from Profile_Functions import Login
            self.frame_options = Frame(self.main_Frame, bg=self.main_Color)
            self.frame_options.grid(column=0, row=2, columnspan=2)
            Login(self.frame_options, self.main_Color, self.variable_profile)

        elif self.variable_profile.name == 'Profile':
            # This function needs to be written
            pass

    # This part of program is responsible to direct the user's input to the respective app
    def app_executing(self, *args):
        self.root.resizable(1, 1)

        if self.variable_apps.name == 'Clock':
            import time
            from Clock import ClockApp as App
        elif self.variable_apps.name == 'Alarm':
            from Alarm import Alarm as App
            import time, winsound
            sys.path.append('Music')
        elif self.variable_apps.name == 'Mario':
            from Mario import MarioApp as App
        elif self.variable_apps.name == 'Palette':
            from Palette import PaletteApp as App

        self.main_Frame.destroy()
        self.main_Frame = Frame(self.root, bg=self.main_Color)
        self.main_Frame.pack()
        self.root.geometry(App.xy)
        App(self.main_Frame)


if __name__ == '__main__':
    constructor = Tk()
    inst = Program(constructor)
    constructor.mainloop()

