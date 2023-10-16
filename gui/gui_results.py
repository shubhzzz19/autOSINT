import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import *
from apis.typo_sqaut import run_dnstwist


# Create GUI
class Result:
    def __init__(self, win, fake_domain):
        self.root = win
        self.root.title("Results")
        w = 1200
        h = 650
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2 - 40
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # Create fonts
        fnt1 = ("Times New Roman", 45, "bold")
        fnt2 = ("Times New Roman", 25, "bold")
        fnt3 = ("Times New Roman", 20, "bold")
        fnt4 = ("Times New Roman", 18, "bold")
        fnt5 = ("Times New Roman", 14, "bold")

        # Create String Var
        name = StringVar()
        address = StringVar()
        mobile = StringVar()
        date_fly = StringVar()
        time_fly = StringVar()
        from1 = StringVar()
        destination = StringVar()
        passeneger = StringVar()
        price = StringVar()

        # Create label display the app name
        self.label = Label(self.root, text=fake_domain, font=fnt5, fg="#443565")
        self.label.place(x=370, y=50)

        self.root.mainloop()
