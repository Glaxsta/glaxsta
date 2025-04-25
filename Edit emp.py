from customtkinter import *

from tkinter import PhotoImage, Label
from tkinter import ttk, messagebox
import database # type: ignore
from datetime import datetime
from tkcalendar import Calendar, DateEntry # type: ignore
import tkinter as tk
import subprocess

def home():
    subprocess.Popen(["python", r"C:\Users\Jhon Harold\OneDrive\Documentos\PAYROLL\PROGRESS\BACKHOME.py"])
    window.destroy()

def show_all():
    treeview_data()
    SearchEntry.delete(0,END)
    Searchbox.set('Search By')


def search_employee():
    if SearchEntry.get()=='':
        messagebox.showerror('Error', 'Enter value to search')
    elif Searchbox.get()=='Search By':
        messagebox.showerror('Error', 'Please select an option')
    else:
        searched_data=database.search(Searchbox.get(),SearchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END, values=employee)
        



def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        database.delete(identry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is deleted')
        

def update_em():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select input to make changes')
    else:
        database.update(identry.get(), First_nameentry.get(), Middle_nameentry.get(), Last_name.get(), Age.get(), Genderbox.get(), Designationbox.get(),Date_hired.get_date(), Date_birth.get_date(), Contact.get(), Email.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is updated')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        identry.insert(0,row[0])
        First_nameentry.insert(0,row[1])
        Middle_nameentry.insert(0,row[2])
        Last_name.insert(0,row[3])
        Age.insert(0,row[4])
        Genderbox.set(row[5])
        Designationbox.set(row[6])
        Date_hired.set_date(row[7])
        Date_birth.set_date(row[8])
        Contact.insert(0,row[9])
        Email.insert(0,row[10])
    
def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)
    First_nameentry.delete(0,END)
    Middle_nameentry.delete(0,END)
    Last_name.delete(0,END)
    Age.delete(0,END)
    Genderbox.set('Male')
    Designationbox.set('Proprietor')
    Contact.delete(0,END)
    Email.delete(0,END)

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END, values=employee)


def add_employee():
    if identry.get()==''or First_nameentry.get()=='' or Middle_nameentry.get()=='' or Last_name.get()=='' or Age.get()=='' or Genderbox.get()=='' or Designationbox.get()==''  or Contact.get()=='' or Email.get()=='':
        
        messagebox.showerror('Error', 'All Field are required') 
    elif database.id_exists(identry.get()):
        messagebox.showerror('Error',' Id Already exists')
        
    else:
        formatted_date_birth = Date_birth.get_date()
        formatted_date_hired = Date_hired.get_date()

        database.insert(identry.get(), First_nameentry.get(), Middle_nameentry.get(), Last_name.get(), Age.get(), Genderbox.get(), Designationbox.get(),formatted_date_hired, formatted_date_birth, Contact.get(), Email.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is added')
        
    
    
    
window=CTk()
window.geometry("600x400+100+100")
window.resizable(True, True)
window.title("ADD EMPLOYEE")
window.after(100, lambda: window.state('zoomed'))


        
leftframe=CTkFrame(window) # you can add fg="color"
leftframe.grid(row=1, column = 0)
leftframe.place(x=5,y=35)

idlabel=CTkLabel(leftframe,text='ID',font=('arial',18,'bold'))
idlabel.grid(row=1,column=1, padx=20,pady=20, sticky='w')

identry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
identry.grid(row=1,column=100)

First_namelabel=CTkLabel(leftframe,text='First name',font=('arial',18,'bold'))
First_namelabel.grid(row=2,column=1, padx=20,pady=20,sticky='w')

First_nameentry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
First_nameentry.grid(row=2,column=100)

Middle_namelabel=CTkLabel(leftframe,text='Middle name',font=('arial',18,'bold'))
Middle_namelabel.grid(row=3,column=1, padx=20,pady=20,sticky='w')
                    #+1
Middle_nameentry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
Middle_nameentry.grid(row=3,column=100)
                    #+1
Last_nameentry=CTkLabel(leftframe,text='Last name',font=('arial',18,'bold'))
Last_nameentry.grid(row=4,column=1, padx=20,pady=20,sticky='w')
                    #+1
Last_name=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
Last_name.grid(row=4,column=100)

Age=CTkLabel(leftframe,text='Age',font=('arial',18,'bold'))
Age.grid(row=5,column=1, padx=20,pady=20,sticky='w')
                    #+1
Age=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
Age.grid(row=5,column=100)

Gender=CTkLabel(leftframe,text='Gender',font=('arial',18,'bold'))
Gender.grid(row=6,column=1, padx=20,pady=20,sticky='w')
Gender_options=['Male','Female']
Genderbox=CTkComboBox(leftframe,values=Gender_options,width=180,font=('arial',18,'bold'),state="readonly")
Genderbox.grid(row=6,column=100)

Designation=CTkLabel(leftframe,text='Position',font=('arial',18,'bold'))
Designation.grid(row=7,column=1, padx=20,pady=20,sticky='w')
Designation_options=['Proprietor','Head Technician','Technician']
Designationbox=CTkComboBox(leftframe,values=Designation_options,width=180,font=('arial',18,'bold'),state="readonly")
Designationbox.grid(row=7,column=100)

Hired_label = CTkLabel(leftframe, text='Date of Hired', font=('arial', 18, 'bold'))
Hired_label.grid(row=8, column=1, padx=20, pady=20, sticky='w')

Date_hired = DateEntry(leftframe, width=18, font=('arial', 15), background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
Date_hired.grid(row=8, column=100)

Birth_label = CTkLabel(leftframe, text='Date of Birth', font=('arial', 18, 'bold'))
Birth_label.grid(row=9, column=1, padx=20, pady=20, sticky='w')

Date_birth = DateEntry(leftframe, width=18, font=('arial', 15), background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
Date_birth.grid(row=9, column=100)


Contactlabel=CTkLabel(leftframe,text='Contact',font=('arial',18,'bold'))
Contactlabel.grid(row=10,column=1, padx=20,pady=20,sticky='w')
                    #+1
Contact=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
Contact.grid(row=10,column=100)

Emaillabel=CTkLabel(leftframe,text='Email',font=('arial',18,'bold'))
Emaillabel.grid(row=11,column=1, padx=20,pady=20,sticky='w')
                    #+1
Email=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
Email.grid(row=11,column=100)

right=CTkFrame(window)
right.grid(row=1, column = 2)
right.place(x=400,y=35)


Search_options=['ID','Last_name','Age','Gender','Designation','Contact','Email']
Searchbox=CTkComboBox(right,values=Search_options,state='readonly')
Searchbox.grid(row=0,column=0)
Searchbox.set('Search By')

SearchEntry = CTkEntry(right)
SearchEntry.grid(row=0,column=1)

SearchButton = CTkButton(right,text='Search', width=100,command=search_employee)
SearchButton.grid(row=0,column=2)

ShowallButton = CTkButton(right,text='Show All', width=100, command=show_all)
ShowallButton.grid(row=0,column=3)

tree=ttk.Treeview(right,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['column'] = ('Id', 'First name', 'Middle name', 'Last name','Age','Gender','Designation','Date of Hired','Date of Birth','Contact','Email')

tree.heading('Id',text='ID')
tree.heading('First name',text='First name')
tree.heading('Middle name',text='Middle name')
tree.heading('Last name',text='Last name')
tree.heading('Age',text='Age')
tree.heading('Gender',text='Gender')
tree.heading('Designation',text='Designation')
tree.heading('Contact',text='Contact')
tree.heading('Email',text='Email')
tree.heading('Date of Hired',text='Date of Hired')
tree.heading('Date of Birth',text='Date of Birth')

tree.config(show='headings')

tree.column('Id',width=60)
tree.column('First name',width=140)
tree.column('Middle name',width=140)
tree.column('Last name',width=140)
tree.column('Age',width=50)
tree.column('Gender',width=100)
tree.column('Designation',width=120)
tree.column('Contact',width=100)
tree.column('Email',width=260)
tree.column('Date of Hired',width=120)
tree.column('Date of Birth',width=120)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',10,'bold'))
style.configure('Treeview', font=('arial',10,'bold'),rowheight=50, background = '#161C30',foreground='white')


Scrollbar=ttk.Scrollbar(right,orient=VERTICAL,command=tree.yview)
Scrollbar.grid(row=1,column=4,sticky='ns')

Scrollbar=ttk.Scrollbar(right,orient=VERTICAL,)
Scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=Scrollbar.set)

right1 = tk.Frame(window, bg="Black")
right1.grid(row=1, column=2)
right1.place(x=1140, y=900)

# Create a label with colored text and background
companyname = tk.Label(
    right1,
    text='FUSIONLINK NETWORK AND DATA SOLUTIONS',
    font=('arial', 25, 'bold'),
    fg="Blue",  # Font color (text color)
    bg="black"  # Background color of the label
)

# Grid placement
companyname.grid(row=11, column=1, padx=8, pady=8, sticky='w')





#img_path = PhotoImage(file=r"C:\Users\Jhon Harold\Downloads\company_logo_resized.png")
#bg_image=tkinter.Label(window,image=img_path,bg="black").place(x=60,y=10,width=350,height=350)



############### BUTTON #################


buttonFrame=CTkFrame(window, fg_color='#161C30')
buttonFrame.grid(row=3,column=0,columnspan=4)
buttonFrame.place(x=700,y=650)



new_button=CTkButton(buttonFrame, text='New Employee',width=160,corner_radius=15, command=lambda: clear(True))
new_button.grid(row=0,column=0, pady=5)

add_button=CTkButton(buttonFrame, text='Add Employee',width=160,corner_radius=15, command = add_employee)
add_button.grid(row=0,column=2, pady=5)

update_button=CTkButton(buttonFrame, text='Update Employee',width=160,corner_radius=15, command=update_em)
update_button.grid(row=0,column=4, pady=5)

delete_button=CTkButton(buttonFrame, text='Delete Employee',width=160,corner_radius=15, command=delete_employee)
delete_button.grid(row=0,column=6, pady=5)

home_button=CTkButton(buttonFrame, text='Home',width=160,corner_radius=15, command=home)
home_button.grid(row=0,column=8, pady=5)

treeview_data()

window.bind('<ButtonRelease>',selection)
   
   
   
  
window.mainloop()

