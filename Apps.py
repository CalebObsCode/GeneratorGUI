import tkinter
import random
import string
import pyperclip
from PIL import ImageTk, Image




# Generate a random password based on the length of the password provided by the user
def generate_password():
    password = ""
    DIGITS = string.digits
    LETTERS = string.ascii_letters
    SYMBOLS = string.punctuation
    UPCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase


    for i in range(password_length_entry.get()):
        password += random.choice(DIGITS + LETTERS + SYMBOLS + UPCASE + LOWERCASE)
    getPassword.set(password)




# Function used to copy the password to the clipboard
def copy_password():
    if getPassword.get() != "":
        pyperclip.copy(getPassword.get())
        messageboxes = tkinter.Label(master, text='Password copied', font='Ubuntu 12',width=15)
        messageboxes.place(x=305, y=220)
    else:
        messageboxes = tkinter.Label(master, text='Nothing to copy', font='Ubuntu 12', width=15)
        messageboxes.place(x=305, y=220)




# Function used to clear the password entry field
def clear_password():
    getPassword.set("")
    messageboxes = tkinter.Label(master, text='Password cleared', font='Ubuntu 12', width=15)
    messageboxes.place(x=305, y=220)


def save_password():
    Password_Array = []
    if getPassword.get() != "":
        Password_Array.append(getPassword.get())
        with open('Generated Passwords.txt', 'a') as f:
            for item in Password_Array:
                f.write("%s\n" % item)
        messageboxes = tkinter.Label(master, text='Password saved', font='Ubuntu 12', width=15)
        messageboxes.place(x=305, y=220)
    else:
        messageboxes = tkinter.Label(master, text='Nothing to save', font='Ubuntu 12', width=15)
        messageboxes.place(x=305, y=220)




master = tkinter.Tk()
master.title('Password Generator')
master.geometry('750x420')
master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))


# Center app icon in window
img = ImageTk.PhotoImage(Image.open("lock.jpeg"))



# Create label for app icon
app_icon = tkinter.Label(master, image=img)
app_icon.pack()


# Prompt for password length
getPassword = tkinter.StringVar()
password_length = tkinter.Label(master, text='Password Length:')
password_length.pack()


# Create entry field for password length
password_length_entry = tkinter.IntVar()
length = tkinter.Spinbox(master, from_=8, to=40, textvariable=password_length_entry)
length.pack(pady=10)




# Create label for password
password_label = tkinter.Label(master, text='Generated Password:')
password_label.pack()


# Create entry field for password
password_entry = tkinter.Entry(master, textvariable=getPassword)
password_entry.pack()


# Button to call generate_password function
generate_button = tkinter.Button(master, text='Generate', command=generate_password)
generate_button.pack(padx=50,pady=5,side=tkinter.LEFT)


# Button to call copy_password function
copy_button = tkinter.Button(master, text='Copy', command=copy_password)
copy_button.pack(padx=50,pady=5,side=tkinter.LEFT)

# Button to call clear_password function
clear_button = tkinter.Button(master, text='Clear', command=clear_password)
clear_button.pack(padx=50,pady=5,side=tkinter.RIGHT)


# Button to call a Save Password function that will save the password to a text file on the user computer
save_button = tkinter.Button(master, text='Save', command=save_password)
save_button.pack(padx=50,pady=5,side=tkinter.RIGHT)





# mainloop is used to display the window
master.mainloop()


