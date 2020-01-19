from tkinter import *
import tkinter as tk
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

def main():

    #window
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Tkinter Login Form')

    #username label and text entry box
    Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
    Label(tkWindow,text="Password").grid(row=1, column=0)  
    password = StringVar()
    Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

    validate = partial(validateLogin, username, password)

    #login button
    Button(tkWindow, text="Login", command=validate).grid(row=4, column=0)  

    tkWindow.mainloop()


# main()


LARGE_FONT= ("Verdana", 12)

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
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=100)

        button = tk.Button(self, text="Log In",
                            command=lambda: controller.show_frame(LogIn))
        button.pack()

        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame(Register))
        button2.pack()


class LogIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Log In Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=100)

        #username label and text entry box
        username_label = tk.Label(self, text="User Name: ")
        username_label.grid(row=0, column=0)
        username_label.pack()
        username = tk.StringVar()
        username_entry = tk.Entry(self, textvariable=username) 
        username_entry.pack()

        #password label and password entry box
        password_label = tk.Label(self,text="Password: ")
        password_label.grid(row=1, column=0)
        password_label.pack()  
        password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=password, show='*')
        password_entry.pack()  

        validate = partial(validateLogin, username, password)

        # trying to make circle
        canvas = tk.Canvas(self, width=300, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_arc(30, 30, 250, 250, start=0, extent=90, fill="red")
        canvas.create_arc(30, 30, 250, 250, start=-90, extent=90, fill="blue")
        canvas.create_arc(30, 30, 250, 250, start=-180, extent=90, fill="green")
        canvas.create_arc(30, 30, 250, 250, start=-270, extent=90, fill="white")

        # #login button
        submit_button = tk.Button(self, text="Login", command=validate)
        submit_button.pack()

        # buttons for navigating between windows
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=LEFT, pady=20)

        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame(Register))
        button2.pack(side=LEFT, pady=20)



class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register page!", font=LARGE_FONT)
        label.pack(pady=10,padx=100)

        # buttons for navigating between windows
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=LEFT)

        button2 = tk.Button(self, text="Log In",
                            command=lambda: controller.show_frame(LogIn))
        button2.pack(side=LEFT)

        


app = Main()
app.mainloop()