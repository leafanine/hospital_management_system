#!/usr/bin/env python
# coding: utf-8

# In[35]:


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import pandas as pd

#connection to database
connection=None
host_name= "localhost"
user_name= "root"
user_password= "enkidu@99ER"
try:
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password
    )
    print("MySQL connection success")
except Error as err:
    print(f"Error: '{err}'")
    
#creation of a database
cursor=connection.cursor()
query="CREATE DATABASE hospital_records;"
try:
    cursor.execute(query)
    connection.commit()
    print("query succcessful")
except Error as err:
    print(f"Error: '{err}'")
    
query="USE hospital_records;"
try:
    cursor.execute(query)
    connection.commit()
    print("using hospital_records now")
except Error as err:
    print(f"Error: '{err}'")
    
#creating a table to store data
cursor= connection.cursor()
create_tb= """CREATE TABLE all_patients (
patientID VARCHAR(80),
name VARCHAR(80),
doctorName VARCHAR(80),
DiseaseName VARCHAR(80),
bloodPressure VARCHAR(40),
spo VARCHAR(40),
weight VARCHAR(20),
height VARCHAR(20),
date varchar(20),
age VARCHAR(20),
gender VARCHAR(20)
);"""
try:
    cursor.execute(create_tb)
    print("Table created successfully")
except Error as err:
    print(f"Error: '{err}'")

#button functions
def prescription():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","all fields needed.")
    else:
        cursor=connection.cursor()
        cursor.execute("insert into all_patients values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
        patientID.get(),
        name.get(),
        doctorName.get(),
        DiseaseName.get(),
        bloodPressure.get(),
        spo.get(),
        weight.get(),
        height.get(),
        date.get(),
        age.get(),
        gender.get()
        ))
    connection.commit()
    fetch_data()
    messagebox.showinfo("Successful","All data saved successfully.")
    
def fetch_data():
    cursor=connection.cursor()
    cursor.execute("select * from all_patients")
    rows=cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        connection.commit()

def get_data(event=''):
    cursor_row=table.focus()
    data=table.item(cursor_row)
    row=data['values']
    patientID.set(row[0])
    name.set(row[1])
    doctorName.set(row[2])
    DiseaseName.set(row[3])
    bloodPressure.set(row[4])
    spo.set(row[5])
    weight.set(row[6])
    height.set(row[7])
    date.set(row[8])
    age.set(row[9])
    gender.set(row[10])

def text_prescription():
    txt.insert(END,'Disease:\t\t\t'+DiseaseName.get()+'\n')
    txt.insert(END,'Blood Pressure:\t\t\t'+bloodPressure.get()+'\n')
    txt.insert(END,'Oxygen:\t\t\t'+spo.get()+'\n')
    
def delete():
    cursor=connection.cursor()
    querry=('delete from all_patients where Reference= %s')
    value=(patientID.get(),)
    cursor.execute(querry,value)
    connection.commit()
    fetch_data()
    messagebox.showinfo('Deleted','Patient data is gone.')
    
def clear():
    patientID.set('')
    name.set('')
    doctorName.set('')
    DiseaseName.set('')
    bloodPressure.set('')
    spo.set('')
    weight.set('')
    height.set('')
    date.set('')
    age.set('')
    gender.set('')
    txt.delete(1.0,END)
    
def exit():
    confirm = messagebox.askyesno('Confirmation','You want to exit?')
    if confirm>0:
        app.destroy()
        return
        
#frontend
app = Tk()
app.state('zoomed')
app.config(bg='black')
# hospital management system heading
Label(app,text="Hospital Management System",font='impack 31 bold',bg='gray',fg='white').pack(fill='x')
#information frame
frame1 = Frame(app,bd='15',relief=RIDGE)
frame1.place(x = 0,y = 54,width=1540,height=450)
#frame for patient information
lf1 = LabelFrame(frame1,bd='5',text='Patient Information',bg='white',fg='blue',font='ariel 12 bold')
lf1.place(x=10,y=0,width=900,height=420)
#label for patient information
Label(lf1,text='Patient ID',font='ariel 12',bg='white',fg='green').place(x=5,y=10)
Label(lf1,text='Name Of Patient',font='ariel 12',bg='white').place(x=5,y=60)
Label(lf1,text='Doctor Name',font='ariel 12',bg='white').place(x=5,y=110)
Label(lf1,text='Disease Name',font='ariel 12',bg='white').place(x=5,y=160)
Label(lf1,text='Blood Pressure',font='ariel 12',bg='white').place(x=5,y=210)
Label(lf1,text='SPO2',font='ariel 12',bg='white').place(x=5,y=260)
Label(lf1,text='Weight',font='ariel 12',bg='white').place(x=5,y=310)
Label(lf1,text='Height',font='ariel 12',bg='white').place(x=5,y=360)
Label(lf1,text='Date',font='ariel 12',bg='white').place(x=650,y=10)
Label(lf1,text='Age',font='ariel 12',bg='white').place(x=650,y=60)
Label(lf1,text='Gender',font='ariel 12',bg='white').place(x=650,y=110)

#variables that contain data
patientID=StringVar()
name=StringVar()
doctorName=StringVar()
DiseaseName=StringVar()
bloodPressure=StringVar()
spo=StringVar()
weight=StringVar()
height=StringVar()
date=StringVar()
age=StringVar()
gender=StringVar()

#--------------Entry Field For Information--------------------
e1 = Entry(lf1,bd='5',font='impack 13',textvariable=patientID)
e1.place(x=160,y=10,width=300)

e2 = Entry(lf1,bd='5',font='impack 13',textvariable=name)
e2.place(x=160,y=60,width=300)

e3 = Entry(lf1,bd='5',font='impack 13',textvariable=doctorName)
e3.place(x=160,y=110,width=300)

e4 = Entry(lf1,bd='5',font='impack 13',textvariable=DiseaseName)
e4.place(x=160,y=160,width=300)

e5 = Entry(lf1,bd='5',font='impack 13',textvariable=bloodPressure)
e5.place(x=160,y=210,width=300)

e6 = Entry(lf1,bd='5',font='impack 13',textvariable=spo)
e6.place(x=160,y=260,width=300)

e7 = Entry(lf1,bd='5',font='impack 13',textvariable=weight)
e7.place(x=160,y=310,width=300)

e8 = Entry(lf1,bd='5',font='impack 13',textvariable=height)
e8.place(x=160,y=360,width=300)

e9 = Entry(lf1,bd='5',font='impack 13',textvariable=date)
e9.place(x=725,y=10,width=150)

e10 = Entry(lf1,bd='5',font='impack 13',textvariable=age)
e10.place(x=725,y=60,width=150)

e11 = Entry(lf1,bd='5',font='impack 13',textvariable=gender)
e11.place(x=725,y=110,width=150)

#-----------------------------------------------------
#label for prescription
lf2 = LabelFrame(frame1,bd='5',text='Prescription',bg='white',fg='blue',font='ariel 12 bold')
lf2.place(x=912,y=0,width=600,height=420)
#textbox for prescription
txt = Text(lf2,font='impack 12 bold',width=40,height=30,bg='pink')
txt.pack(fill=BOTH)
#details frame
frame2 = Frame(app,bd='15',relief=RIDGE)
frame2.place(x='0',y='500',width=1540,height=250)

#----------------buttons for function---------------------
dlt = Button(app,text='Delete',font='ariel 15 bold',bg='red',fg='white',bd='5',cursor='hand2',command=delete)
dlt.place(x=0,y=750,width=280)

pres = Button(app,text='Prescription',font='ariel 15 bold',bg='violet',fg='white',bd='5',cursor='hand2',command=text_prescription)
pres.place(x=280,y=750,width=280)

save = Button(app,text='Save Patient Data',font='ariel 15 bold',bg='green',fg='white',bd='5',cursor='hand2',command=prescription)
save.place(x=560,y=750,width=420)

clear = Button(app,text='Clear',font='ariel 15 bold',bg='violet',fg='white',bd='5',cursor='hand2', command=clear)
clear.place(x=980,y=750,width=280)

exit = Button(app,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd='5',cursor='hand2',command=exit)
exit.place(x=1260,y=750,width=280)

#---------------------------------------------------------
#---------scroll bar for prescription data----------
scrollx=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scrollx.pack(side='bottom',fill='x')

scrolly=ttk.Scrollbar(frame2,orient=VERTICAL)
scrolly.pack(side='right',fill='y')

table = ttk.Treeview(frame2,columns=('id','name','date','age','gender','disis','bl_pre','spo2','wght','height'),xscrollcommand=scrolly.set,yscrollcommand=scrollx.set)
scrollx = ttk.Scrollbar(command=table.xview())
scrolly = ttk.Scrollbar(command=table.yview())
#---------------------------------------------------


#-------heading for prescription data----------
table.heading('id',text='Patient ID')
table.heading('name',text='Patient Name')
table.heading('date',text='Date')
table.heading('age',text='Age')
table.heading('gender',text='Gender')
table.heading('disis',text='Disease Name')
table.heading('bl_pre',text='Blood Pressure')
table.heading('spo2',text='SPO2')
table.heading('wght',text='Weight')
table.heading('height',text='Height')
table['show'] = 'headings'
table.pack(fill=BOTH,expand=1)
#---------------------------------------------

#-------Table column width-------
table.column('id',width=100)
table.column('name',width=100)
table.column('date',width=100)
table.column('age',width=100)
table.column('gender',width=100)
table.column('disis',width=100)
table.column('bl_pre',width=100)
table.column('spo2',width=100)
table.column('wght',width=100)
table.column('height',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
#--------------------------------

mainloop()


# In[ ]:





# In[ ]:




