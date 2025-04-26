import pymysql
from tkinter import messagebox
from datetime import datetime



def connect_database():
    global mycursor ,conn
    

    try:
        conn=pymysql.connect(host='localhost',user='root',password='1234')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Something went wrong')
        conn = None
        mycursor = None
        return 
        
    mycursor.execute('CREATE DATABASE IF NOT EXISTS test_3')
    mycursor.execute('USE test_3')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS data (id VARCHAR(30), F_name VARCHAR(50), MI_name VARCHAR(50), Last_name VARCHAR(50), Age VARCHAR(30), Gender VARCHAR(10), Designation  VARCHAR(50), formatted_Date_hired DATE, formatted_Date_birth DATE, Contact VARCHAR(20), Email VARCHAR(50))''')
    
    

def insert(id, F_name, MI_name, Last_name, Age, Gender, Designation, Date_hired, Date_birth, Contact, Email):
    global mycursor, conn
    try:
        # Convert input dates into MySQL DATE format
        formatted_Date_birth = Date_birth  # Already datetime.date
        formatted_Date_hired = Date_hired 
    except ValueError:
        messagebox.showerror('Error', 'Invalid date format. Use YYYY-MM-DD')
        return



    # Ensure correct number of columns
    mycursor.execute('INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(id, F_name, MI_name, Last_name, Age, Gender, Designation, formatted_Date_hired, formatted_Date_birth, Contact, Email) )

    conn.commit()
    
def id_exists(id):
    global mycursor, conn
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    global mycursor, conn
    mycursor.execute('SELECT * from DATA')
    result=mycursor.fetchall()
    return result

def update(id, new_F_name, new_MI_name, new_Last_name, new_Age, new_Gender, new_Designation, new_formatted_Date_hired, new_formatted_Date_birth, new_Contact, new_Email):
    global mycursor, conn
    mycursor.execute('UPDATE data SET F_name=%s, MI_name=%s, Last_name=%s, Age=%s, Gender=%s, Designation=%s, formatted_Date_hired=%s, formatted_Date_birth=%s, Contact=%s, Email=%s WHERE id=%s',( new_F_name, new_MI_name, new_Last_name, new_Age, new_Gender, new_Designation, new_formatted_Date_hired, new_formatted_Date_birth, new_Contact, new_Email,id))
    conn.commit()
    
def delete(id):
    global mycursor, conn
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()
    
def search(option,value):
    global mycursor, conn
    mycursor.execute (f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result
    
    
    
connect_database()
