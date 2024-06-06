
import tkinter
from tkinter import *
import page2
root=tkinter.Tk()


root.geometry("600x500")
root.title("Registration")
lblHeading=Label(root,text="Student Registration Form ",font=('impact',30),fg='orange')
lblHeading.place(x=500,y=200)

sUserName=StringVar()
studentID=StringVar()
sCourse=StringVar()
sPaymentStatus=StringVar()

#1
lblValue1=Label(root,text="UserName :")
lblValue1.place(x=550,y=300)
txtValue1=Entry(root,textvariable=sUserName)
txtValue1.place(x=650,y=300)

#student Id
lblValue1=Label(root,text="Student ID :")
lblValue1.place(x=550,y=350)
txtValue1=Entry(root,textvariable=studentID)
txtValue1.place(x=650,y=350)

#2
lblValue2=Label(root,text="course : ")
lblValue2.place(x=550,y=400) 
dropdown=OptionMenu(root,sCourse,'Bsc','B.tech','B.com','MCA','MBA')
dropdown.place(x=650,y=400)
#3
lblValue3=Label(root,text="PaymentStatus : ")
lblValue3.place(x=550,y=450)
dropdown=OptionMenu(root,sPaymentStatus,'yes','no')
dropdown.place(x=650,y=450)

def Login():
    username=sUserName.get()
    course=sCourse.get()
    paymentstatus=sPaymentStatus.get()
    if page2.login(username,course,paymentstatus):
        print("Registration successfully")
    else:
        print("Invalid username and course and paymentstatus")
        
#button
btnadd=Button(root,text="submit",command=Login,bg="skyblue")
btnadd.place(x=650,y=500)

