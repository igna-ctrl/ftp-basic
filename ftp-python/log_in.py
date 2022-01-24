# Log in window
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("FTP Interface")
frame = ttk.Frame(root, padding="5 5 5 5")
frame.grid()

ttk.Label(frame, text="Username").grid(column=0, row=0)
username = StringVar()
username_input=ttk.Entry(frame, textvariable=username).grid(column=1, row=0)

ttk.Label(frame, text="Password").grid(column=0, row=1)
password = StringVar()
password_input = ttk.Entry(
    frame, textvariable=password, show="*").grid(column=1, row=1)


ttk.Button(frame, text="Submit", command=printer).grid(column=3, row=3)