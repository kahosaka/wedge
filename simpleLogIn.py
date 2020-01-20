from tkinter import *
import tkinter as tk
from functools import partial
import wheel as w
import slice as s

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

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

        # bind keyboard input to this frame
        # self.bind('<Key>', lambda a : self.key_press(a))
        self.focus_set()
        self.bind("<Key>", self.key_press)

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

        # create canvas
        canvas = tk.Canvas(self, width=300, height=300)
        canvas.pack(fill="both", expand=True)
        # create wheel
        wheel = w.Wheel()
        wheel.create(canvas)


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

    # function to process keyboard input
    def key_press(self, event):
        key = event.char 
        print(key, 'is pressed')
  



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

        

def main():
    app = Main()
    app.mainloop()

main()






# canvas.create_arc(30, 30, 250, 250, start=0, extent=90, outline="red", width=7.0)
        # canvas.create_arc(30, 30, 250, 250, start=90, extent=90, outline="blue", width=7.0)
        # canvas.create_arc(30, 30, 250, 250, start=180, extent=90, outline="green", width=7.0)
        # canvas.create_arc(30, 30, 250, 250, start=270, extent=90, outline="black", width=7.0)

        # canvas.create_arc(30, 30, 250, 250, start=0, extent=36, fill="red2")
        # canvas.create_arc(30, 30, 250, 250, start=36, extent=36, fill="blue")
        # canvas.create_arc(30, 30, 250, 250, start=72, extent=36, fill="forest green")
        # canvas.create_arc(30, 30, 250, 250, start=108, extent=36, fill="white")
        # canvas.create_arc(30, 30, 250, 250, start=144, extent=36, fill="purple1")
        # canvas.create_arc(30, 30, 250, 250, start=180, extent=36, fill="dark turquoise")
        # canvas.create_arc(30, 30, 250, 250, start=216, extent=36, fill="DarkOrange1")
        # canvas.create_arc(30, 30, 250, 250, start=252, extent=36, fill="saddle brown")
        # canvas.create_arc(30, 30, 250, 250, start=288, extent=36, fill="yellow")
        # canvas.create_arc(30, 30, 250, 250, start=324, extent=36, fill="gray")
        # canvas.create_text(200, 100, text="a")