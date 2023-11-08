import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import *
import datetime

# Create GUI
class Result:
       def __init__(self, win, fake_domain,IP,org_info,phone):
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
              
              self.v = Scrollbar(self.root, orient='vertical')
              # Creating file for typo sqaut 
              current_datetime = datetime.datetime.now()
              formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
              if fake_domain:
                     with open(f'D:/autOSINT/results/typo_sqaut_{formatted_datetime}.txt', 'w') as file:
                            file.write(fake_domain)
                     self.label = Label(self.root, text='Fake Domains for the typosqauting: ', font=fnt5, fg="#443565")
                     self.label.place(x=70, y=50)
                     self.typo_text=Text(self.root,yscrollcommand=self.v.set, font=fnt5, fg="#443565")
                     self.typo_text.insert("1.0", fake_domain)
                     self.v.config(command=self.typo_text.yview)
                     self.typo_text.place(x=180,y=50)
              # Creating file for IP lookup
              if IP:
                     with open(f'D:/autOSINT/results/ip_lookup_{formatted_datetime}.txt', 'w') as file:
                            file.write(IP)
                     self.label = Label(self.root, text=f'View the IP loop up in D:/autOSINT/results/ip_lookup_{formatted_datetime}.txt', font=fnt5, fg="#443565")
                     self.label.place(x=70, y=90)
              
              # Creating file for Organization Information
              if org_info:
                     with open(f'D:/autOSINT/results/org_info_{formatted_datetime}.txt', 'w') as file:
                            file.write(org_info)
                     self.label = Label(self.root, text=f'View the Organization Information in D:/autOSINT/results/org_info_{formatted_datetime}.txt', font=fnt5, fg="#443565")
                     self.label.place(x=70, y=140)           
              
              # Creating file for Phone Information
              if phone:
                     with open(f'D:/autOSINT/results/Phone_info_{formatted_datetime}.txt', 'w') as file:
                            file.write(phone)
                     self.label = Label(self.root, text=f'View the Phone Information in D:/autOSINT/results/Phone_info_{formatted_datetime}.txt', font=fnt5, fg="#443565")
                     self.label.place(x=70, y=180)   
              self.root.mainloop()
