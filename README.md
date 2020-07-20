# Wedge (See Report and Poster for more info)
While passwords are meant to be secure ways for people to gain authorization and access, there are many ways in which passwords get stolen. Some simple examples are video recording, a program that logs keystrokes to then decipher the password, or simply standing behind and watching the person type in their password. User authentication is one of the most important and fundamental components in computer security systems, therefore it is important to ensure that it is a well protected process. This software combines both graphical and textual passwords to ensure a secure and effective login process that is immune to shoulder surfing, keylogging, and video recordings.

# Authors
Jeanie Chen and Kiana Hosaka

# Commands
```
$ python3 main.py

```

# Installations and System Requirements
This application works with Python3 only, thus the user should make sure their machine has the correct version of Python installed first.

This application has been tested on macOS Mojave and macOS Catalina. It is not compatible with Dark Mode.

Download our Wedge repository to your own machine and navigate into the directory.

# Directions
Downloading Repository
- Go to our Github repo website https://github.com/kahosaka/wedge
- Click “Clone or Download” and copy the URL
- Open terminal and navigate into the directory where user wishes to place the repository
- Run the command “git clone https://github.com/kahosaka/wedge.git”

Running Wedge Application
- Complete the steps in “Downloading Repo”
- In the terminal and in the Wedge directory, run the command “python3 main.py”
- A window named “Wedge” will open

Home Page
- Two options that a user can do on the home page: log in or register
- Clicking on the “Register” button will take the user to the Registration page
- Clicking on the “Log In” button will take the user to the Log In page

Registration
- Once on the Registration page, type in the chosen username in the text box underneath the text “Username”
- Type in a chosen password using only the characters specified above the password text box
- Choose a color from the drop down menu
- Remember username, password, and chosen color in order to log in
- Submit account information and wait for the pop up window to inform if registration was successful
- If successful, click the “Log In” button to go to the log in page
- If unsuccessful, restart steps 1-3

Login
- Once on the Log In page, type in username in the text box and hit the “enter/return” on the keyboard
- Find the slice on the wheel that has chosen color
- Rotate that colors counterclockwise or clockwise using the keys “a” or “d” respectively until color is on a slice that contains the first character of user's password
- Select the inner or outer character using the keys “s” or “w” respectively
- Repeat steps 2-4 for every character of the password until password has been completely entered
- Click the “Login” button to complete the log in process
- A pop up window will appear informing log in success or failure
