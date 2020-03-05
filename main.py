from tkinter import *
import tkinter as tk
from tkinter import messagebox
from functools import partial
import wheel as w
import slice as s

"""
Routing between pages idea from https://pythonprogramming.net/change-show-new-frame-tkinter/
Project inspired by Nevon Projects https://nevonprojects.com/graphical-password-to-avoid-shoulder-surfing/
"""


LARGE_FONT= ("Verdana", 12)
COLORS = ["red2", "DarkOrange1", "blue", "forest green", "purple1", "white", "saddle brown"
        , "dark turquoise", "yellow", "dim gray"]
DISPLAY_PASSWORD_COORDS = [100, 20]


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(10, weight=1)
        container.grid_columnconfigure(10, weight=1)

        self.frames = {}

        for F in (StartPage, LogIn, Register):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home\nWelcome to Wedge!", font=LARGE_FONT)
        label.pack(pady=10,padx=100)

        button = tk.Button(self, text="Log In",
                            command=lambda: controller.show_frame(LogIn))
        button.pack()

        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame(Register))
        button2.pack()

class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register page!", font=LARGE_FONT)
        label.pack(pady=10,padx=100)

        # save user chosen color
        self.color = None

        #username label and text entry box
        username_label = tk.Label(self, text="User Name: ")
        # username_label.grid(row=0, column=0)
        username_label.pack()
        username = tk.StringVar()
        username_entry = tk.Entry(self, textvariable=username)
        username_entry.pack()

        #password label and password entry box
        password_label = tk.Label(self,text="Password: ")
        # password_label.grid(row=1, column=0)
        password_label.pack()
        label = tk.Label(self,text="(Please create your password using \n these characters: 0-9, a-j)")
        label.config(font=("Helvetica", 11))
        label.pack()
        password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=password)
        password_entry.pack()

        # create drop down menu
        color_label = tk.Label(self,text="Choose Color: ")
        # color_label.grid(row=1, column=0)
        color_label.pack()
        color = tk.StringVar()
        color.set("red2")
        drop_down = tk.OptionMenu(self, color, *COLORS, command=self.getColor)
        drop_down.pack()


        # button to submit user info
        # will trigger a function that saves everything to file
        # in the format: username password color
        submit_button = tk.Button(self, text="Submit", command=lambda: self.saveInfo(username.get(), password.get(), username_entry, password_entry))
        submit_button.pack()

        # buttons for navigating between windows
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=LEFT)

        button2 = tk.Button(self, text="Log In",
                            command=lambda: controller.show_frame(LogIn))
        button2.pack(side=LEFT)

    # function to get chosen color from drop down menu
    def getColor(self, value):
        self.color = value


    # function to save created user info into a file for future log in validation
    def saveInfo(self, username, password, user_entry, pass_entry):
        try:
            # first check if username exists already
            with open("credentials.txt", "r") as f:
                for line in f:
                    # line parsing
                    x = line.split(' ')
                    # check if username exists
                    if x[0] == username:
                        # prompt user to choose another username
                        messagebox.showinfo("Retry", "Username already exists, please choose another one")
                        user_entry.delete(0, END)
                        pass_entry.delete(0, END)
                        f.close()
                        return
            f.close()
            user_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showinfo("Success", "Registration success!")
            with open("credentials.txt", "a") as f:
                f.write(username + ' ')
                f.write(password + ' ')
                f.write(self.color + '\n')
        except Exception as e:
            print(e)
        finally:
            f.close()


class LogIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In Page!\n", font=LARGE_FONT)
        label.pack(pady=10,padx=100)

        # keep track of current user's color and password
        self.user_color = None
        self.user_password = None
        self.current_password = ""

        # create log in window components
        self.createWindow(controller)

    # function that creates all components of the log in page
    def createWindow(self, controller):
        #username label and text entry box
        username_label = tk.Label(self, text="User Name: ")
        # username_label.grid(row=0, column=0)
        username_label.pack()
        username = tk.StringVar()
        username_entry = tk.Entry(self, textvariable=username)
        # user has to press enter/return key after typing in their username
        username_entry.bind("<Return>", lambda event: self.checkUsername(username.get()))
        username_entry.pack()

        #password label and password entry box
        password_label = tk.Label(self,text="Password: ")
        # password_label.grid(row=1, column=0)
        password_label.pack()
        # password = tk.StringVar()
        # password_entry = tk.Entry(self, textvariable=password, show='*')
        # password_entry.pack()

        password_canvas = tk.Canvas(self, width=300, height=30)
        password_canvas.pack()

        # create canvas
        canvas = tk.Canvas(self, width=300, height=300)
        canvas.pack(fill="both", expand=True)
        # create wheel
        wheel = w.Wheel()
        wheel.create(canvas)

        # bind keyboard input to this frame
        self.focus_set()
        self.bind("<Key>", lambda event: self.keyPress(event, wheel, canvas, password_canvas))

        #login button
        # need to bind this with a function that validates credentials
        validate = partial(self.validateLogin, password_canvas)
        submit_button = tk.Button(self, text="Login", command=validate)
        submit_button.pack()

        # buttons for navigating between windows
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=LEFT, pady=20)

        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame(Register))
        button2.pack(side=LEFT, pady=20)

    # function that handles keyboard input
    def keyPress(self, event, wheel, canvas, password_canvas):
        key = event.char
        # print(key, 'is pressed')

        # if key pressed is w (up), user chooses outer letter
        if key == "w":
            index = 1

            # need to show a * on the screen, find the slice that is chosen,
            # get chosen char from slice,
            # add char to current password
            slice = wheel.getSlice(self.user_color)
            char = slice.getCharacter((index))
            self.current_password += char
            password_canvas.create_text(DISPLAY_PASSWORD_COORDS[0], DISPLAY_PASSWORD_COORDS[1], text="*")
            DISPLAY_PASSWORD_COORDS[0] += 10

        # if key pressed is s (down), user chooses inner letter
        if key == "s":
            index = 0
            # need to show a * on the screen, find the slice that is chosen,
            # get chosen char from slice,
            # add char to current password
            slice = wheel.getSlice(self.user_color)
            char = slice.getCharacter((index))
            self.current_password += char
            password_canvas.create_text(DISPLAY_PASSWORD_COORDS[0], DISPLAY_PASSWORD_COORDS[1], text="*")
            DISPLAY_PASSWORD_COORDS[0] += 10

        # if key pressed is a (left), user chooses to rotate wheel left
        if key == "a":
            direction = -1
            wheel.updateColorsSlices(canvas, direction)

        # if key pressed is d (right), user chooses to rotate wheel right
        if key == "d":
            direction = 1
            wheel.updateColorsSlices(canvas, direction)

    # function to check entered username and retrieve this user's actual password and color
    def checkUsername(self, username):
        try:
            with open("credentials.txt", "r") as f:
                for line in f:
                    # line parsing
                    x = line.split(' ')
                    # check if username matches
                    if x[0] == username:
                        # keep this user's password and color for comparison later
                        self.user_password = x[1]
                        if len(x) > 3:
                            temp = x[2:]
                            self.user_color = " ".join(temp)
                            self.user_color = self.user_color[:-1]
                        else:
                            self.user_color = x[2]
                            self.user_color = self.user_color[:-1]

            self.focus()
        except Exception as e:
            print(e)
        finally:
            f.close()
        return

    # function to validate login using previously saved user_password to compare against
    # what the user has entered via the wheel
    def validateLogin(self, password_canvas):
        if self.user_password == self.current_password:
            # log in successful!
            messagebox.showinfo("Success", "Log In Success!")
        else:
            # password not correct
            messagebox.showinfo("Fail", "Password Incorrect. Please try again")
            password_canvas.delete("all")
            # reset password
            self.current_password = ""



def main():
    app = Main()
    app.title("Wedge")
    app.mainloop()

if __name__ == "__main__":
    main()
