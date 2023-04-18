# NEEDS TO HAVE CHECKBUTTON OF THE CREATE MENU SETTINGS INSERT IN THE DB REGISTRY

# VERIFY THE BEST WAY TO MANAGE THE FUNCTIONS WHAT ARE NEEDED
# GET AN WAY TO CONTOUR THE BUTTON IMAGE USING PILLOW OR CREATING A NEW ALGORITHM
import _tkinter
from tkinter import *
import shelve


# This class contains the menu where users make login
class Login(object):
    def __init__(self, frame_options, main_color, variable):
        # Assigns local variables to instance variables
        self.frame_options = frame_options
        self.variable = variable
        self.main_color = main_color

        # Create and set widgets that contains users information
        self.font_login_screen = ('Sans Serif', '14', 'normal')
        self.request_login = Label(self.frame_options, text='Login', bg=main_color, font=self.font_login_screen)
        self.request_login.grid(column=1, row=0, columnspan=3)

        self.entry_login = Entry(self.frame_options)
        self.entry_login.grid(column=1, row=1, columnspan=3)

        self.request_password = Label(self.frame_options, text='Password', bg=main_color, font=self.font_login_screen)
        self.request_password.grid(column=1, row=2, columnspan=3)

        self.entry_password = Entry(self.frame_options)
        self.entry_password.grid(column=1, row=3, columnspan=3)

        # Importing the function new_button
        from creating_button_function import new_button

        # The button of login created by the function new_button with a label structure
        # Boolean Variable created to activate the function login attempt
        self.variable_login = BooleanVar(value=False)
        self.variable_login.trace('w', self.login_attempt)
        self.login_button = new_button('Images/button_login.png', self.frame_options, self.main_color,
                                       self.variable_login)
        self.login_button.grid(column=1, row=4)

        # The button to create a user created by the function new_button with a label structure
        # Boolean Variable created to activate the function to_create_menu
        self.variable_create = BooleanVar(value=False)
        self.variable_create.trace('w', self.to_create_menu)
        self.create_button = new_button('Images/button_create.png', self.frame_options, self.main_color,
                                        self.variable_create)
        self.create_button.grid(column=2, row=4)

        # That's a void label what will be filled with the program return about login
        self.void_label = Label(self.frame_options, text='', width=70, height=1, bg=self.main_color)
        self.void_label.grid(column=1, row=5, columnspan=2)

        # The Checkbutton what will remind password if it was pressed before the login
        self.var_cb_user = True
        # This function is responsible to invert the variable var_cb_user value every time the checkbutton were pressed
        remind_user = lambda: not self.var_cb_user
        self.login_checkbutton = Checkbutton(self.frame_options, text='Remind User', command=remind_user(),
                                             bg=self.main_color, activebackground=self.main_color)
        self.login_checkbutton.grid(column=1, row=6, columnspan=2)

        # This is the function responsible to check if the var_cb_user were marked at the last login and if it was the
        # login information will be filled up
        db = shelve.open('log.db')
        try:
            if db['Last User'][0] == True:
                self.entry_login.insert(0, db['Last User'][1])
                self.entry_password.insert(0, db['Last User'][2])
        except KeyError:
            db['Last User'] = (False, False, False)
        finally:
            db.close()

    # Thi function is for the login in database and change the main variable Boolean to call Checker_variable function
    def login_attempt(self, *args):
        db = shelve.open('log.db')
        try:
            if db[self.entry_login.get()][1] == self.entry_password.get():
                db['Last User'] = (self.var_cb_user, self.entry_login.get(), self.entry_password.get())
                self.frame_options.destroy()
                self.variable.name = 'Apps'
                self.variable.set(True)
            elif self.entry_password.get() == '':
                self.void_label.configure(text='Void Password')
            else:
                self.void_label.configure(text='Wrong Password')
        except KeyError:
            self.void_label.configure(text="Email isn't registered")
        finally:
            db.close()

    # This function is responsible to return if create button were pressed. It opens the create menu
    def to_create_menu(self, *args):
        self.frame_options.destroy()
        self.variable.name = 'Create'
        self.variable.set(True)


# This class contains the menu where users creating them profiles
class Create(object):
    def __init__(self, frame_options, main_color, variable):
        # Assigns local variables to instance variables
        self.frame_options = frame_options
        self.variable = variable
        self.main_color = main_color

        # Create and set widgets that contains users information
        self.label_name = Label(self.frame_options, text='Name', bg=main_color)
        self.label_name.grid(row=0, column=1)
        self.entry_name = Entry(self.frame_options)
        self.entry_name.grid(row=1, column=1)

        self.label_email = Label(self.frame_options, text='E-mail', bg=main_color)
        self.label_email.grid(row=2, column=1)
        self.entry_email = Entry(self.frame_options)
        print(self.frame_options)
        self.entry_email.grid(row=3, column=1)

        self.label_password = Label(self.frame_options, text='Password', bg=main_color)
        self.label_password.grid(row=4, column=1)
        self.entry_password = Entry(self.frame_options)
        self.entry_password.grid(row=5, column=1)

        self.check_button_remind = Checkbutton(self.frame_options, text='Remember-me', bg=main_color,
                                               activebackground=main_color)
        self.check_button_remind.grid(row=6, column=1)

        # ERROR OCCURS HERE
        self.variable_create_user = BooleanVar(value=False, name='not_created')
        self.variable_create_user.trace('w', self.call)
        '''variable_create_user NEEDS TO CALL DATABASE'''

        from creating_button_function import new_button
        self.create_button = new_button('Images/button_create.png', self.frame_options, self.main_color,
                                        self.variable_create_user)
        self.create_button.grid(row=7, column=1, pady=2)

        self.void_frame = Frame(self.frame_options)
        self.void_frame.grid(column=1, row=8)

    # ERROR OCCURS HERE
    def call(self, *args):
        print('it was called')

    # ERROR OCCURS HERE
    # This function contains the login information checker
    def data_base(self, *args):
        db = shelve.open('log.db')
        try:
            db[self.entry_email.get()]
            self.label_error = Label(self.void_frame, text='This Email is Already Registered')
            self.label_error.pack()

        except _tkinter.TclError:
            # Import and uses a function what verify all users mistakes in user's creating menu
            from word_checker import email_features, password_features, name_features
            list_mistakes = [email_features(self.entry_email.get()), password_features(self.entry_password.get()),
                             name_features(self.entry_name.get())]
            # Shows existent mistakes in case of a not response for list_mistakes index
            for i in range(len(list_mistakes)):
                if not list_mistakes[i][0]:
                    self.label_error = Label(self.void_frame, text=list_mistakes[i][1])
                    self.label_error.pack()
                    continue
                # In event of no mistakes the user account is created and the login screen is set again
                if i == len(list_mistakes)-1:
                    db[self.entry_email.get()] = [self.entry_name.get(), self.entry_password.get()]
                    self.frame_options.destroy()
                    self.variable.name = 'Login'
                    self.variable.set(True)
        else:
            print('not happens')
        finally:
            db.close()
        # Such case of login's name doesn't exist this creates an exception

