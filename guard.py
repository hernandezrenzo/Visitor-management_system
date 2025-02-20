#Village Visitor Management System
#For the Guards

from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk, messagebox
import tkinter

vvms = Tk()
vvms.title("Village Visitor Management System")
vvms.geometry("760x430")
# img = PhotoImage(file= 'D:\\programn\\python\\Visitor_Village_Management_System\\vms.png')
# vvms.iconphoto(False, img)
vvms.configure(bg="#949398")

def today():
  wcm.destroy()
  VVMS.destroy()
  VTVL.destroy()
  history.destroy()
  EXIT.destroy()

  def attributes():
    def update():
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

      if (lbl_id=="" or lbl_name=="" or lbl_age=="" or lbl_gndr=="" or lbl_adres=="" or lbl_cntct=="" or lbl_plt=="" or lbl_hnv=="" or lbl_date=="" or lbl_in=="" or lbl_out==""):
        MessageBox.showinfo("Update Status", "All fields are required")
      else:
        con = mysql.connect(host="localhost", username="root", password="", database="vvms-tkinter")
        cursor = con.cursor()
        cursor.execute("update vvms set lbl_name='"+ lbl_name +"', lbl_age='"+ lbl_age +"', lbl_gndr='"+ lbl_gndr +"',lbl_adres='"+ lbl_adres +"', lbl_cntct='"+ lbl_cntct +"', lbl_plt='"+ lbl_plt +"', lbl_hnv='"+ lbl_hnv +"', lbl_date='"+ lbl_date +"', lbl_in='"+ lbl_in +"', lbl_out='"+ lbl_out +"' where lbl_id='"+ lbl_id +"'")
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
        ent_out.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Updated Succesfully!");
        con.close();

    def get():
      if (ent_id.get() == ""):
        MessageBox.showinfo("Fetch Status","ID is compolsary for delete")
      else:
        con = mysql.connect(host="localhost", user="root", password="", database="vvms-tkinter")
        cursor = con.cursor()
        cursor.execute("select * from vvms where lbl_id='"+ ent_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
          ent_name.insert(0, row[1])
          ent_age.insert(0, row[2])
          ent_gndr.insert(0, row[3])
          ent_adres.insert(0, row[4])
          ent_cntct.insert(0, row[5])
          ent_plt.insert(0, row[6])
          ent_hnv.insert(0, row[7])
          ent_date.insert(0, row[8])
          ent_in.insert(0, row[9])
          ent_out.insert(0, row[10])
          con.close();

    def show():
      con = mysql.connect(host="localhost", username="root", password="", database="vvms-tkinter")
      cursor = con.cursor()
      cursor.execute("SELECT lbl_id, lbl_name, lbl_adres, lbl_plt, lbl_hnv, lbl_date, lbl_in, lbl_out FROM vvms")
      records = cursor.fetchall()
      print(records)

      for i, (lbl_id, lbl_name, lbl_adres, lbl_plt, lbl_hnv, lbl_date, lbl_in, lbl_out) in enumerate(records, start=1):
        listbox.insert("", "end", values=(lbl_id, lbl_name, lbl_adres, lbl_plt, lbl_hnv, lbl_date, lbl_in, lbl_out))
        con.close();

    lbl_id = Label(vvms, text="Visitor ID :", font=("Lato", 12), bg="#949398")
    lbl_id.place(x=5, y=10)
    lbl_name = Label(vvms, text="Name :", font=("Lato", 12), bg="#949398")
    lbl_name.place(x=5, y=40)
    lbl_age = Label(vvms, text="Age :", font=("Lato", 12), bg="#949398")
    lbl_age.place(x=5, y=70)
    lbl_gndr = Label(vvms, text="Gender :", font=("Lato", 12), bg="#949398")
    lbl_gndr.place(x=5, y=100)
    lbl_adres = Label(vvms, text="Address :", font=("Lato", 12), bg="#949398")
    lbl_adres.place(x=5, y=130)
    lbl_cntct = Label(vvms, text="Contact No. :", font=("Lato", 12), bg="#949398")
    lbl_cntct.place(x=5, y=160)

    lbl_plt = Label(vvms, text="Plate No. :", font=("Lato", 12), bg="#949398")
    lbl_plt.place(x=340, y=10)
    lbl_hnv = Label(vvms, text="House No. Visiting :", font=("Lato", 10), bg="#949398")
    lbl_hnv.place(x=340, y=41)
    lbl_date = Label(vvms, text="Date :", font=("Lato", 12), bg="#949398")
    lbl_date.place(x=340, y=70)
    lbl_in = Label(vvms, text="Time In :", font=("Lato", 12), bg="#949398")
    lbl_in.place(x=340, y=100)
    lbl_out = Label(vvms, text="Time Out :", font=("Lato", 12), bg="#949398")
    lbl_out.place(x=340, y=130)

    ent_id = Entry(vvms, font=("Lato", 11), width=26)
    ent_id.place(x=100, y=11)
    ent_name = Entry(vvms, font=("Lato", 11), width=26)
    ent_name.place(x=100, y=41)
    ent_age = Entry(vvms, font=("Lato", 11), width=26)
    ent_age.place(x=100, y=71)
    ent_gndr = Entry(vvms, font=("Lato", 11), width=26)
    ent_gndr.place(x=100, y=101)
    ent_adres = Entry(vvms, font=("Lato", 11), width=26)
    ent_adres.place(x=100, y=131)
    ent_cntct = Entry(vvms, font=("Lato", 11), width=26)
    ent_cntct.place(x=100, y=161)

    ent_plt = Entry(vvms, font=("Lato", 11), width=32)
    ent_plt.place(x=460, y=11)
    ent_hnv = Entry(vvms, font=("Lato", 11), width=32)
    ent_hnv.place(x=460, y=41)
    ent_date = Entry(vvms, font=("Lato", 11), width=32)
    ent_date.place(x=460, y=71)
    ent_in = Entry(vvms, font=("Lato", 11), width=32)
    ent_in.place(x=460, y=101)
    ent_out = Entry(vvms, font=("Lato", 11), width=32)
    ent_out.place(x=460, y=131)

    get = Button(vvms, text="GET", font=("Lato", 11, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=get)
    get.place(x=300, y=185)
    update = Button(vvms, text="UPDATE", font=("Lato", 11, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=update)
    update.place(x=400, y=185)

    cols = ('Visitor ID', 'Name', 'Address', 'Plate No.', 'House No. Visiting','Date', 'Time In', 'Time_out')
    listbox = ttk.Treeview(vvms, height=7, columns=cols, show='headings')

    for col in cols:
      listbox.heading(col, text=col)
      listbox.grid(row=1, column=0)
      listbox.place(x=1, y=220)

    back = Button(vvms, text="EXIT", font=("Lato", 11, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=ext)
    back.place(x=695, y=390)
    show()
    listbox.bind('<Double-Button-1>,Delete')
  attributes()

def out():
  wcm.destroy()
  VVMS.destroy()
  VTVL.destroy()
  history.destroy()
  EXIT.destroy()
  
  greet = Label(vvms, text="Visitors who left the village :", font=("Lato", 15, "bold", "italic"), bg="#949398", fg="#FFE77A")
  greet.place(x=5, y=5)

  def v_out():
    def show():
      con = mysql.connect(host="localhost", username="root", password="", database="vvms-tkinter")
      cursor = con.cursor()
      cursor.execute("SELECT lbl_name, lbl_adres, lbl_plt, lbl_hnv, lbl_date, lbl_in, lbl_out FROM vvms")
      records = cursor.fetchall()
      print(records)

      for i, (lbl_name, lbl_adres, lbl_plt, lbl_hnv, lbl_date, lbl_in, lbl_out) in enumerate(records, start=1):
        listbox.insert("", "end", values=(lbl_name, lbl_adres, lbl_plt, lbl_hnv, lbl_date, lbl_in, lbl_out))
        con.close();

    cols = ('Name', 'Address', 'Plate No.', 'House No.','Date', 'Time In', 'Time_out')
    listbox = ttk.Treeview(vvms, height=8 ,columns=cols, show='headings')

    for col in cols:
      listbox.heading(col, text=col)
      listbox.grid(row=1, column=0)
      listbox.place(x=1, y=50)

    back = Button(vvms, text="EXIT", font=("Lato", 11, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=ext)
    back.place(x=695, y=385)
    show()
    listbox.bind('<Double-Button-1>,Delete')
  v_out()

def ext():
  ext = tkinter.messagebox.askyesno("VVMS", "Confirm is Yes or No?")
  if ext > 0:
    vvms.destroy()
    return

wcm = Label(vvms, text="WELCOME TO", font=("Lato", 35), bg="#949398", fg="#FFE77A")
wcm.place(x=235, y=20)
VVMS = Label(vvms, text="VVMS", font=("Lato", 40, "bold"), bg="#949398", fg="#FFE77A")
VVMS.place(x=315, y=75)

VTVL = Button(vvms, text="View Log", font=("Lato", 25, "bold"), bd=5, bg="#949398", fg="#FFE77A", command=today)
VTVL.place(x=305, y=170)
history = Button(vvms, text="View History", font=("Lato", 25, "bold"), bd=5, bg="#949398", fg="#FFE77A", command=out)
history.place(x=275, y=260)
EXIT = Button(vvms, text="EXIT", font=("Lato", 13, "bold"), bd=3, bg="#949398", fg="#FFE77A", command=ext)
EXIT.place(x=695, y=385)

vvms.mainloop()