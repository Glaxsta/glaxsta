from tkinter import*
from tkinter import messagebox

import pymysql #pip install pymysql


class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title(" Fusion Link Network and Data Solution Payroll Management System ")
        self.root.geometry("135x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text = "Fusion Link Network and Data Solution Payroll Management System",font=("times new roman", 40, "bold"),bg ="#262626",fg ="tan").place(x=0,y=0,relwidth=1)
        
        #.................................Frame 1......................................#################################
        #================================Frame 1 Variables=======================
        self.var_Code=StringVar()
        self.var_Designation=StringVar()
        self.var_Birthday=StringVar()
        self.var_Name=StringVar()
        self.var_DOJ=StringVar()
        self.var_Age=StringVar()
        self.var_EXP=StringVar()
        self.var_Gender=StringVar()
        self.var_ID=StringVar()
        self.var_Email=StringVar()
        self.var_Contact=StringVar()
        self.var_Hired=StringVar()
        self.var_Status=StringVar()
        
        
        
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="linen")
        Frame1.place(x=10,y=70,width=890,height=620)
        title2=Label(Frame1,text = "EMPLOYEE INFORMATION ",font=("times new roman", 20, "bold"),bg ="lightgray",fg ="black", anchor='w',padx=10).place(x=0,y=0,relwidth=1)
        
        #++++++++++++++++++++++++++++++++ ROW 1 +++++++++++++++++++++++++++++++++++++++
        lbl_Code=Label(Frame1,text = "Employee I.D ",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=70)
        txt_Code=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Code,bg ="lightyellow",fg ="black").place(x=250,y=80, width=200)
        btn_search=Button(Frame1,text="Search", font=("times new roman",20),bg="white",fg="black").place(x=460,y=80,height=25)
        #++++++++++++++++++++++++++++++++ ROW 2 +++++++++++++++++++++++++++++++++++++++
        lbl_Designation=Label(Frame1,text = "Designation",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=120)
        txt_Designation=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Designation,bg ="lightyellow",fg ="black").place(x=220,y=130, width=200)
        
        lbl_Birthday=Label(Frame1,text = "Birth Date",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=440,y=120) #change the x
        txt_Birthday=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Birthday,bg ="lightyellow",fg ="black").place(x=650,y=130) #change the y
        
        #++++++++++++++++++++++++++++++++ ROW 3 +++++++++++++++++++++++++++++++++++++++
        lbl_Name=Label(Frame1,text = "Name",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=160) #change the y by 40
        txt_Name=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Name,bg ="lightyellow",fg ="black").place(x=220,y=170, width=200) #change the y by 40
        
        lbl_D_O_J=Label(Frame1,text = "D.O.J",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=440,y=160) #change the y by 40
        txt_D_O_J=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_DOJ,bg ="lightyellow",fg ="black").place(x=650,y=170) #change the y by 40
        
        #++++++++++++++++++++++++++++++++ ROW 4 +++++++++++++++++++++++++++++++++++++++
        lbl_Age=Label(Frame1,text = "Age",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=200) #change the y by 40
        txt_Age=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Age,bg ="lightyellow",fg ="black").place(x=220,y=210, width=200) #change the y by 40
        
        lbl_EXP=Label(Frame1,text = "Experience",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=440,y=200) #change the y by 40
        txt_EXP=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_EXP,bg ="lightyellow",fg ="black").place(x=650,y=210) #change the y by 40
        
        #++++++++++++++++++++++++++++++++ ROW 5 +++++++++++++++++++++++++++++++++++++++
        lbl_Gender=Label(Frame1,text = "Sex",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=240) #change the y by 40
        txt_Gender=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Gender,bg ="lightyellow",fg ="black").place(x=220,y=250, width=200) #change the y by 40
        
        lbl_ID=Label(Frame1,text = "I.D",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=440,y=240) #change the y by 40
        txt_ID=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_ID,bg ="lightyellow",fg ="black").place(x=650,y=250) #change the y by 40
        
        #++++++++++++++++++++++++++++++++ ROW 6 +++++++++++++++++++++++++++++++++++++++
        lbl_Email=Label(Frame1,text = "Email",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=280) #change the y by 40
        txt_Email=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Email,bg ="lightyellow",fg ="black").place(x=220,y=290, width=200) #change the y by 40
        
        lbl_Contact=Label(Frame1,text = "Contact no.",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=440,y=280) #change the y by 40
        txt_Contact=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Contact,bg ="lightyellow",fg ="black").place(x=650,y=290) #change the y by 40
        
        #++++++++++++++++++++++++++++++++ ROW 7 +++++++++++++++++++++++++++++++++++++++
        lbl_Hired=Label(Frame1,text = "Hired",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=320) #change the y by 40
        txt_Hired=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Hired,bg ="lightyellow",fg ="black").place(x=220,y=330, width=200) #change the y by 40
        
        lbl_Status=Label(Frame1,text = "Status",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=440,y=320) #change the y by 40
        txt_Status=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_Status,bg ="lightyellow",fg ="black").place(x=650,y=330) #change the y by 40
        
        #++++++++++++++++++++++++++++++++ ROW 8 +++++++++++++++++++++++++++++++++++++++
        lbl_Address=Label(Frame1,text = "Address",font=("times new roman", 20, "bold"),bg ="linen",fg ="black").place(x=10,y=400) #change the y by 80
        self.txt_Address=Text(Frame1,font=("times new roman", 15),bg ="lightyellow",fg ="black") #change the y by 80
        self.txt_Address.place(x=170,y=410,width=600,height=150)
        
        #.................................Frame 2......................................##########################################
        #================================Frame 2 Variables=======================
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_Daily_salary=StringVar()
        self.var_total_days=StringVar()
        self.var_absents=StringVar()
        self.var_medical=StringVar()
        self.var_funds=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        
        
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="linen")
        Frame2.place(x=900,y=70,width=580,height=300)
        
        title2=Label(Frame2,text = "Employee Salary Details ",font=("times new roman", 20, "bold"),bg ="lightgray",fg ="black", anchor='w',padx=10).place(x=0,y=0,relwidth=1)
         
        #++++++++++++++++++++++++++++++++ ROW 1 +++++++++++++++++++++++++++++++++++++++
        lbl_month=Label(Frame2,text = "Month",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=10,y=80) 
        txt_month=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_month,bg ="lightyellow",fg ="black").place(x=90,y=85, width=100) 
        lbl_year=Label(Frame2,text = "Year",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=210,y=80) 
        txt_year=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_year,bg ="lightyellow",fg ="black").place(x=265,y=85, width=60) 
        lbl_Daily_salary=Label(Frame2,text = "Daily Salary",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=350,y=80) 
        txt_Daily_salary=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_Daily_salary,bg ="lightyellow",fg ="black").place(x=470,y=85, width=50) 
        
        #++++++++++++++++++++++++++++++++ ROW 2 +++++++++++++++++++++++++++++++++++++++
        lbl_total_days=Label(Frame2,text = "Total Days",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=10,y=105)
        txt_total_days=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_total_days,bg ="lightyellow",fg ="black").place(x=120,y=110, width=70) 
        lbl_absents=Label(Frame2,text = "Absents",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=210,y=105)
        txt_absents=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_absents,bg ="lightyellow",fg ="black").place(x=295,y=110, width=60) 
        #++++++++++++++++++++++++++++++++ ROW 3 +++++++++++++++++++++++++++++++++++++++
        lbl_medical=Label(Frame2,text = "Medical",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=10,y=130) 
        txt_medical=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_medical,bg ="lightyellow",fg ="black").place(x=90,y=135, width=100)
        lbl_funds=Label(Frame2,text = "Provident fund",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=210,y=130)
        txt_funds=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_funds,bg ="lightyellow",fg ="black").place(x=350,y=135, width=150)
        #++++++++++++++++++++++++++++++++ ROW 4 +++++++++++++++++++++++++++++++++++++++
        lbl_convence=Label(Frame2,text = "Convence",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=10,y=155) 
        txt_convence=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_convence,bg ="lightyellow",fg ="black").place(x=100,y=160, width=90) 
        lbl_net_salary=Label(Frame2,text = "Net Salary",font=("times new roman", 15, "bold"),bg ="linen",fg ="black").place(x=210,y=155) 
        txt_net_salary=Entry(Frame2,font=("times new roman", 10),textvariable=self.var_net_salary,bg ="lightyellow",fg ="black").place(x=350,y=160, width=150)
        
        btn_clear=Button(Frame2,text="Clear", font=("times new roman",20),bg="red",fg="black").place(x=480,y=250,height=25)
        btn_save=Button(Frame2,text="Save", font=("times new roman",20),bg="green",fg="black").place(x=390,y=250,height=25)
        btn_calculate=Button(Frame2,text="Calculate",command =self.calculate, font=("times new roman",12),bg="orange",fg="black").place(x=305,y=250,height=25)
        
         #.................................Frame 3......................................##########################################
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="linen")
        Frame3.place(x=900,y=380,width=580,height=310)
        
        ############################### Calculator frame ########################################
        
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
        
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
            
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
            
        Cal_frame=Frame(Frame3,bg = "white", bd=2, relief=RIDGE)
        Cal_frame.place(x=2, y=2, width=247, height=300)
        
            
            
        
        
        txt_result=Entry(Cal_frame, bg="lightyellow",textvariable=self.var_txt,font=(" times new roman", 20, "bold"),justify=RIGHT).place(x=0, y=0,relwidth=1, height =52)
        
        #ROW1
        btn_7=Button(Cal_frame, text='7',command=lambda:btn_click(7),font=("times new roman", 15, "bold" )).place(x=2, y=53, w=60, h=60)
        btn_8=Button(Cal_frame, text='8',command=lambda:btn_click(8),font=("times new roman", 15, "bold" )).place(x=62, y=53, w=60, h=60)
        btn_9=Button(Cal_frame, text='9',command=lambda:btn_click(9),font=("times new roman", 15, "bold" )).place(x=122, y=53, w=60, h=60)
        btn_div=Button(Cal_frame, text='/',command=lambda:btn_click('/'),font=("times new roman", 15, "bold" )).place(x=182, y=53, w=60, h=60)            
        
        #ROW2
        btn_4=Button(Cal_frame, text='4',command=lambda:btn_click(4),font=("times new roman", 15, "bold" )).place(x=2, y=113, w=60, h=60)
        btn_5=Button(Cal_frame, text='5',command=lambda:btn_click(5),font=("times new roman", 15, "bold" )).place(x=62, y=113, w=60, h=60)
        btn_6=Button(Cal_frame, text='6',command=lambda:btn_click(6),font=("times new roman", 15, "bold" )).place(x=122, y=113, w=60, h=60)
        btn_pro=Button(Cal_frame, text='*',command=lambda:btn_click('*'),font=("times new roman", 15, "bold" )).place(x=182, y=113, w=60, h=60)
        
        #ROW3
        btn_1=Button(Cal_frame, text='1',command=lambda:btn_click(1),font=("times new roman", 15, "bold" )).place(x=2, y=173, w=60, h=60)
        btn_2=Button(Cal_frame, text='2',command=lambda:btn_click(2),font=("times new roman", 15, "bold" )).place(x=62, y=173, w=60, h=60)
        btn_3=Button(Cal_frame, text='3',command=lambda:btn_click(3),font=("times new roman", 15, "bold" )).place(x=122, y=173, w=60, h=60)
        btn_sub=Button(Cal_frame, text='-',command=lambda:btn_click('-'),font=("times new roman", 15, "bold" )).place(x=182, y=173, w=60, h=60)
        
        #ROW4
        btn_0=Button(Cal_frame, text='0',command=lambda:btn_click(0),font=("times new roman", 15, "bold" )).place(x=2, y=233, w=60, h=60)
        btn_decimal=Button(Cal_frame, text='.',command=lambda:btn_click('.'),font=("times new roman", 15, "bold" )).place(x=62, y=233, w=60, h=60)
        btn_add=Button(Cal_frame, text='+',command=lambda:btn_click('+'),font=("times new roman", 15, "bold" )).place(x=122, y=233, w=60, h=60)
        btn_equal=Button(Cal_frame, text='=',command=result,font=("times new roman", 15, "bold" )).place(x=182, y=233, w=60, h=60)
        
        ########################## SALARY ############################
        
        sal_frame=Frame(Frame3,bg = "linen", bd=2, relief=RIDGE)
        sal_frame.place(x=250, y=2, width=323, height=300)
        
        title_sal=Label(sal_frame,text = "SALARY RECIEPT ",font=("times new roman", 20, "bold"),bg ="lightgray",fg ="black", anchor='w',padx=10).place(x=0,y=0,relwidth=1)
        
        sal_frame2=Frame(sal_frame,bg = "white", bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=30, relwidth=1, height=230)
        
        scroll_y=Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)   
        
        self.txt_salary_receipt=Text(sal_frame2, font=("times new roman", 15), bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1 )
        scroll_y.config(command=self.txt_salary_receipt.yview)
        
        btn_print=Button(sal_frame,text="PRINT", font=("times new roman",12),bg="aqua",fg="black").place(x=180,y=262,height=33,width=120)
        
        self.check_connection()
#========================================= START ========================================
    
        
        
    def calculate(self):
        #FRAME 1 VARIABLES
        print(self.var_Code.get(),
        self.var_Designation.get(),
        self.var_Birthday.get(),
        self.var_Name.get(),
        self.var_DOJ.get(),
        self.var_Age.get(),
        self.var_EXP.get(),
        self.var_Gender.get(),
        self.var_ID.get(),
        self.var_Email.get(),
        self.var_Contact.get(),
        self.var_Hired.get(),
        self.var_Status.get(),
        
        #FRAME 2 VARIABLES
        self.var_month.get(),
        self.var_year.get(),
        self.var_Daily_salary.get(),
        self.var_total_days.get(),
        self.var_absents.get(),
        self.var_medical.get(),
        self.var_funds.get(),
        self.var_convence.get(),
        self.var_net_salary.get(),
        self.txt_Address.get('1.0',END)
        )
        
    def calculate (self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_Daily_salary.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            per_day=int(self.var_Daily_salary.get()) * 1
            work_day=int(self.var_total_days.get())-int(self.var_absents.get())
            sal= per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_funds.get())
            addition=int(self.var_convence.get())
            net_salary=sal-deduct+addition
            self.var_net_salary.set(str(round(net_salary,2)))
            
    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost', user='root',password='', db='group3')
            cur=con.cursor()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
               
        
        
        
        
        
        
        
root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
