#Village Visitor Management System
#For the Users/Visitors

import builtins
from tkinter import *
import tkinter
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

vvms = Tk()
vvms.title("Village Visitor Management System")
vvms.geometry("640x430")
# img = PhotoImage(file= 'D:\\programn\\python\\Visitor_Village_Management_System\\vms.png')
#D:\programn\python\Village_Visitor_Management_System
# vvms.iconphoto(False, img)
vvms.resizable(0,0,)
vvms.configure(bg="#949398")

def home():
  def add():
    wcm.destroy()
    VVMS1.destroy()
    btn_add.destroy()
    btn_ext.destroy()

    def attribute():
      def insert():
        lbl_id = ent_id.get()
        lbl_name = ent_name.get();
        lbl_age = ent_age.get();
        lbl_gndr = ent_gndr.get();
        lbl_adres = ent_adres.get();
        lbl_cntct = ent_cntct.get();
        lbl_plt = ent_plt.get();
        lbl_hnv = ent_hnv.get();
        lbl_date = ent_date.get();
        lbl_in = ent_in.get();
        lbl_out = ent_out.get();

        if (lbl_id=="" or lbl_name=="" or lbl_age=="" or lbl_gndr=="" or lbl_adres=="" or lbl_cntct=="" or lbl_plt=="" or lbl_hnv=="" or lbl_date=="" or lbl_in==""):
          MessageBox.showinfo("Adding Status", "All fields are required")
        else:
          con = mysql.connect(host="localhost", username="root", password="", database="vvms-tkinter")
          cursor = con.cursor()
          cursor.execute("insert into vvms values('"+ lbl_id +"','"+ lbl_name +"','"+ lbl_age +"','"+ lbl_gndr +"','"+ lbl_adres +"','"+ lbl_cntct +"','"+ lbl_plt +"','"+ lbl_hnv +"','"+ lbl_date +"','"+ lbl_in +"','"+ lbl_out +"')")
          cursor.execute("commit");

          ent_id.delete(0, 'end')
          ent_name.delete(0, 'end')
          ent_age.delete(0, 'end')
          ent_gndr.delete(0, 'end')
          ent_adres.delete(0, 'end')
          ent_cntct.delete(0, 'end')
          ent_plt.delete(0, 'end')
          ent_hnv.delete(0, 'end')
          ent_date.delete(0, 'end')
          ent_in.delete(0, 'end')
          MessageBox.showinfo("Adding Status", "Added Succesfully!");
          con.close();

      VVMS2 = Label(vvms, text="VVMS", font=("Lato", 35, "bold"), bg="#949398", fg="#FFE77A")
      VVMS2.place(x=5, y=5)

      lbl_id = Label(vvms, text="Visitor ID :", font=("Lato", 12, ), bg="#949398")
      lbl_id.place(x=20, y=60)
      ent_id = Entry(vvms, font=("Lato", 11), width=48)
      ent_id.place(x=185, y=60)

      lbl_name = Label(vvms, text="Name :", font=("Lato", 12, ), bg="#949398")
      lbl_name.place(x=20, y=90)
      ent_name = Entry(vvms, font=("Lato", 11), width=48)
      ent_name.place(x=185, y=90)

      lbl_age = Label(vvms, text="Age :", font=("Lato", 12, ), bg="#949398")
      lbl_age.place(x=20, y=120)
      ent_age = Entry(vvms, font=("Lato", 11), width=48)
      ent_age.place(x=185, y=120)

      lbl_gndr = Label(vvms, text="Gender :", font=("Lato", 12, ), bg="#949398")
      lbl_gndr.place(x=20, y=150)
      ent_gndr = Entry(vvms, font=("Lato", 11), width=48)
      ent_gndr.place(x=185, y=150)

      lbl_adres = Label(vvms, text="Address :", font=("Lato", 12, ), bg="#949398")
      lbl_adres.place(x=20, y=180)
      ent_adres = Entry(vvms, font=("Lato", 11), width=48)
      ent_adres.place(x=185, y=180)

      lbl_cntct = Label(vvms, text="Contact Number :", font=("Lato", 12, ), bg="#949398")
      lbl_cntct.place(x=20, y=210)
      ent_cntct = Entry(vvms, font=("Lato", 11), width=48)
      ent_cntct.place(x=185, y=210)

      lbl_plt = Label(vvms, text="Plate Number :", font=("Lato", 12, ), bg="#949398")
      lbl_plt.place(x=20, y=240)
      ent_plt = Entry(vvms, font=("Lato", 11), width=48)
      ent_plt.place(x=185, y=240)

      lbl_hnv = Label(vvms, text="House No. Visiting :", font=("Lato", 12, ), bg="#949398")
      lbl_hnv.place(x=20, y=270)
      ent_hnv = Entry(vvms, font=("Lato", 11), width=48)
      ent_hnv.place(x=185, y=270)

      lbl_date = Label(vvms, text="Date :", font=("Lato", 12, ), bg="#949398")
      lbl_date.place(x=20, y=300)
      date_format = Label(vvms, text="YYYY-MM-DD :", font=("Lato", 12), bg="#949398")
      date_format.place(x=193, y=298)
      ent_date = Entry(vvms, font=("Lato", 11), width=33)
      ent_date.place(x=320, y=300)

      lbl_in = Label(vvms, text="Time In :", font=("Lato", 12, ), bg="#949398")
      lbl_in.place(x=20, y=330)
      in_format = Label(vvms, text="HH : MM AM/PM :",font=("Lato", 12, ), bg="#949398")
      in_format.place(x=185, y=330)
      ent_in = Entry(vvms, font=("Lato", 11), width=33)
      ent_in.place(x=320, y=330)
      ent_out = Entry(vvms, font=("Lato", 11), width=10)
      ent_out.place(x=1000, y=1000)

      adding = Button(vvms, text="ADD", font=("Lato", 12, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=insert)
      adding.place(x=350, y=390)
      exitt = Button(vvms, text="EXIT", font=("Lato", 12, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=ext)
      exitt.place(x=450, y=390)
    attribute()

  def ext():
    ext = tkinter.messagebox.askyesno("VVMS", "Confirm if Yes or No?")
    if ext > 0:
      vvms.destroy()
      return

  wcm = Label(vvms, text="WELCOME TO", font=("Lato", 35), bg="#949398", fg="#FFE77A")
  wcm.place(x=165, y=20)
  VVMS1 = Label(vvms, text="VVMS", font=("Lato", 40, "bold"), bg="#949398", fg="#FFE77A")
  VVMS1.place(x=250, y=75)
  btn_add = Button(vvms, text="ADD", font=("lato", 16, "bold"), bd=4, bg="#949398", fg="#FFE77A", command=add)
  btn_add.place(x=80, y=270)
  btn_ext = Button(vvms,text="EXIT", font=("lato", 16, "bold"), bd=4, bg="#949398", fg="#FFE77A", command=ext)
  btn_ext.place(x=500, y=270)
home()
vvms.mainloop()