import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import *
from gui.gui_results import Result
from apis.typo_squat import run_dnstwist
from apis.lookup import lookup
from apis.org_details import search_organization_details
from apis.phone import phone_osint


class Main:
       def __init__(self, win):
              self.root = win
              self.root.title("AutOSINT")
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
              fnt6 = ("Times New Roman", 10)
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
              self.label = Label(self.root, text="AutOSINT", font=fnt1, fg="#443565")
              self.label.place(x=480, y=15)
              self.label1 = Label(
              self.root,
              text="A cutting-edge Footprinting software that leverages AI and Machine Learning techniques to extract valuable information about target victims using OSINT",
              font=fnt6,
              fg="#443565",
              )
              self.label1.place(x=240, y=95)
              self.label1 = Label(
              self.root,
              text="(Open Source Intelligence) APIs. The software provides a user-friendly GUI developed with Python Tkinter, enabling users to interact and input their requirements to obtain essential",
              font=fnt6,
              fg="#443565",
              )
              self.label1.place(x=100, y=120)
              self.label1 = Label(
              self.root,
              text="details about the target victims. These details include location information, phone numbers, domain information, and more. AutOSINT offers a powerful and efficient solution for",
              font=fnt6,
              fg="#443565",
              )
              self.label1.place(x=100, y=145)
              self.label1 = Label(
              self.root,
              text="gathering crucial intelligence, aiding in investigations and data analysis.",
              font=fnt6,
              fg="#443565",
              )
              self.label1.place(x=100, y=170)

              self.host = Label(self.root, text="Host:", font=fnt2, fg="#443565")
              self.host.place(x=490, y=200)
              self.e_host = Entry(self.root, width=30, font=fnt4, textvariable=name)
              self.e_host.place(x=600, y=205)

              self.Domain = Label(self.root, text="Domain:", font=fnt2, fg="#443565")
              self.Domain.place(x=445, y=250)
              self.e_Domain = Entry(self.root, width=30, font=fnt4, textvariable=address)
              self.e_Domain.place(x=600, y=255)

              self.ip = Label(self.root, text="Enter IP:", font=fnt2, fg="#443565")
              self.ip.place(x=332, y=300)
              self.e_ip = Entry(self.root, width=30, font=fnt4, textvariable=mobile)
              self.e_ip.place(x=600, y=305)

              self.nm_org = Label(
              self.root, text="Name of Organization:", font=fnt2, fg="#443565"
              )
              self.nm_org.place(x=243, y=350)
              self.e_nm_org = Entry(self.root, width=30, font=fnt4, textvariable=date_fly)
              self.e_nm_org.place(x=600, y=355)

              self.email = Label(self.root, text="E-Mail address:", font=fnt2, fg="#443565")
              self.email.place(x=340, y=400)
              self.e_email = Entry(self.root, width=30, font=fnt4, textvariable=price)
              self.e_email.place(x=600, y=405)

              self.phone = Label(self.root, text="Phone-no:", font=fnt2, fg="#443565")
              self.phone.place(x=340, y=450)
              self.e_phone = Entry(self.root, width=30, font=fnt4, textvariable=time_fly)
              self.e_phone.place(x=600, y=455)

              # Progress Bar
              self.progbar = Progressbar(
              self.root, orient=HORIZONTAL, length=220, mode="determinate"
              )
              self.progbar.place(x=490, y=500)

              self.fetch = Button(
              self.root, text="Fetch", font=fnt4, bg="white", command=self.fetch
              )
              self.fetch.place(x=450, y=555)

              self.exit = Button(
              self.root, text="Exit", font=fnt4, bg="white", command=self.exit_app
              )
              self.exit.place(x=690, y=555)

              self.root.mainloop()

       def fetch(self):
              # Check if all fields are empty
               if (
                     not self.e_host.get()
                     and not self.e_Domain.get()
                     and not self.e_ip.get()
                     and not self.e_nm_org.get()
                     and not self.e_email.get()
                     and not self.e_phone.get()
        ):
        # Show an error message if all fields are empty
                 messagebox.showerror("Error", "Alert! one or more field can be empty, but not all")
               else:
                   self.progbar.start()
                   self.root.after(5000, self.perform_fetch)
                   
       def perform_fetch(self):
              # self.root.destroy()
              self.win = tk.Tk()
              self.app = Result(self.win, fake_domain=str(run_dnstwist(self.e_Domain.get())),IP=lookup((self.e_ip.get())),org_info=search_organization_details(self.e_Domain.get()),phone=str(phone_osint(self.e_phone.get())))
              self.root.mainloop()

       def exit_app(self):
              self.root.destroy()


def test():
       win = tk.Tk()
       app = Main(win)
       win.mainloop()
