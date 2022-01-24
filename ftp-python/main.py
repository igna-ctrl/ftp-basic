from tkinter import *
from tkinter import ttk
from ftplib import FTP


def printer(*args):
    print('Value in username ' + username.get())
    print('Value in username ' + password.get())
    return 1


root = Tk()
root.title("FTP Interface")
frame = ttk.Frame(root, padding="5 5 5 5")
frame.grid()

def response_handler():
    return 0

class Ip_window(ttk.Frame):
    


root.mainloop()
