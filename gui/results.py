import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Create GUI
class Result:
       def __init__(self,win):
              self.root=win
              self.root.title('Booking_Plane_Tickets')
              w = 1200
              h = 650
              sw = self.root.winfo_screenwidth()
              sh = self.root.winfo_screenheight()
              x = (sw - w) / 2
              y = (sh - h) / 2 - 40
              self.root.geometry( '%dx%d+%d+%d' % (w, h, x, y))
              self.root.config(bg="pink")

              #Create fonts
              fnt1 = ("Times New Roman", 45, "bold")
              fnt2 = ("Times New Roman", 25, "bold")
              fnt3 = ("Times New Roman", 20, "bold")
              fnt4 = ("Times New Roman", 18, "bold")
              fnt5 = ("Times New Roman", 14, "bold")

              #Create String Var
              name = StringVar()
              address = StringVar()
              mobile = StringVar()
              date_fly = StringVar()
              time_fly = StringVar()
              from1 = StringVar()
              destination = StringVar()
              passeneger = StringVar()
              price = StringVar()
              
              #Create label display the app name
              self.label = Label(self.root,text='Booking Plane Tickets',font=fnt1,fg='#443565')
              self.label.place(x= 370,y=50)
              #Create label name
              self.label_name = Label(self.root,text='Name:',font=fnt2,fg='#443565')
              self.label_name.place(x=340, y=150)
              #Create label address
              self.label_address = Label(self.root,text='Address:',font=fnt2,fg='#443565')
              self.label_address.place(x=340, y=200)
              #Create label mobile
              self.label_mobile = Label(self.root,text='Mobile:',font=fnt2,fg='#443565')
              self.label_mobile.place(x=340, y=250)   
              #Create label date+
              self.label_date = Label(self.root,text='Date:',font=fnt2,fg='#443565')
              self.label_date.place(x=340, y=300)
              #Create label time
              self.label_time = Label(self.root,text='Time:',font=fnt2,fg='#443565')
              self.label_time.place(x=340, y=350)
              #Create label from

              self.label_from = Label(self.root,text='From:',font=fnt2,fg='#443565')
              self.label_from.place(x=340, y=400)
              #Create label to
              self.label_to = Label(self.root,text='To:',font=fnt2,fg='#443565')
              self.label_to.place(x=340, y=450)
              #Create label price
              self.label_to = Label(self.root,text='Price:',font=fnt2,fg='#443565')
              self.label_to.place(x=340, y=500)
              #Create entry name
              self.e_name = Entry(self.root,font=fnt2,textvariable=name)
              self.e_name.place(x=500,y=155)
              #Create entry addrress
              self.e_address = Entry(self.root,font=fnt2,textvariable=address)
              self.e_address.place(x=500,y=205)
              #Create entry mobile
              self.e_mobile = Entry(self.root,font=fnt2,textvariable=mobile)
              self.e_mobile.place(x=500,y=255)
              #Create entry date fly
              self.e_date= Entry(self.root,font=fnt2,textvariable=date_fly)
              self.e_date.place(x=500,y=305)
              #Create entry time fly
              self.e_time= Entry(self.root,font=fnt2,textvariable=time_fly)
              self.e_time.place(x=500,y=355)
              #Create entry from where
              self.e_from = Entry(self.root,font=fnt2,textvariable=from1)
              self.e_from.place(x=500,y=405)
              #Create entry destination
              self.e_to = Entry(self.root,font=fnt2,textvariable=destination)
              self.e_to.place(x=500,y=455)
              #Create entry price
              self.e_price = Entry(self.root,font=fnt2,textvariable=price)
              self.e_price.place(x=500,y=505)

              self.root.mainloop()

              
