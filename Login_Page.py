from site import makepath
from tkinter import*
from tkinter import messagebox
from tkinter import PhotoImage
import tkinter
import customtkinter # type: ignore
import os
import time
import subprocess
from tkinter import PhotoImage, Label, StringVar, Toplevel, filedialog
from PIL import Image, ImageTk


root = Tk()
root.title("signUp")
root.geometry("930x500")
root.configure(bg='black')
root.resizable(0,0)




def sigin():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password == '1234':
        root.destroy()
        
        def my_function():
            print('VALID')          
                
        # Create main application window
        my_app = customtkinter.CTk()
        my_app.geometry("930x500")
        my_app.title("My App")
        my_app.resizable(width=False, height=False)
        
        def login():
            subprocess.Popen(["python", r"C:\Users\Jhon Harold\OneDrive\Documentos\PAYROLL\PROGRESS\Login_Page.py"])  
            my_app.destroy()
        
        
        def open_script():
            
            subprocess.Popen(["python", r"C:\Users\Jhon Harold\OneDrive\Documentos\PAYROLL\PROGRESS\Edit emp.py"])  
            my_app.destroy()
            
        def open_payslip():
            
            subprocess.Popen(["python", r"C:\Users\Jhon Harold\OneDrive\Documentos\PAYROLL\PROGRESS\Print Payslip.py"])  
            my_app.destroy()
        
        frame = customtkinter.CTkFrame(master=my_app, fg_color="black")
        frame.pack(side="top", fill="both", expand=True)
        
        # Load Image (Ensure it is stored globally to prevent garbage collection)
        img_path = PhotoImage(file=r"C:\Users\Jhon Harold\Downloads\43f3d175-613c-4959-95d5-5e1f465bdc60.png")
        bg_image = Label(my_app, image=img_path)
        bg_image.place(x=100, y=0, width=930, height=453)
        

        # Buttons
        button_1 = customtkinter.CTkButton(master=my_app, text="EDIT EMPLOYEE", command=open_script,font=("",10)) #print("Add Employee Clicked"), font=("", 10))
        button_1.place(x=220, y=400, anchor="ne")

        button_2 = customtkinter.CTkButton(master=my_app, text="PRINT PAYSLIP", command=open_payslip, font=("", 10))
        button_2.place(x=520, y=400, anchor="ne", )

        button_3 = customtkinter.CTkButton(master=my_app, text="PRINT DTR INFORMATION", command=lambda: print("Print DTR Clicked"), font=("", 10))
        button_3.place(x=820, y=400, anchor="ne") 
        
        button_4 = customtkinter.CTkButton(master=my_app, text="LOG OUT", command=login, font=("", 10))
        button_4.place(x=520, y=450, anchor="ne")  
        
        
        my_app.mainloop()
        
    else:
        messagebox.showerror('Invalid', 'Check your password or email')

        # Run the application
        


    
        
    

img_path = PhotoImage(file=r"C:\Users\Jhon Harold\Downloads\company_logo_resized.png")
bg_image=tkinter.Label(root,image=img_path,bg="black").place(x=60,y=10,width=350,height=350)




frame=Frame(root,width=350,height=360,bg='honeydew')
frame.place(x=490,y=50)


heading =Label(frame,text='Sign In', fg='pink',bg='honeydew',font=('Microsoft yahei UI Light',15,'bold'))
heading.place(x=135,y=5)

#====
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='honeydew',font=('Microsoft yahei UI Light',15))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='aqua').place(x=25,y=107)

#====
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='honeydew',show='*',font=('Microsoft yahei UI Light',15))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='aqua').place(x=25,y=177)



#=================

Button (frame,width=39,pady=7,text='Log in', bg="green", fg='darkseagreen',border=0, command=sigin).place(x=35,y=210)






root.mainloop()