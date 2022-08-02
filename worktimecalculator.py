#Import dependencies 
import pandas as pd 
import datetime 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile
import csv
#change the name of the file using time 
import time
start_time = time.time()
current_date = datetime.datetime.now()
# root window
root = tk.Tk()
root.geometry('500x200')
root.resizable(0,0)
root.title('Work Time Calculator v: 0.1 ')

def data():

    try: #tries to read in existing data.csv file
        df = pd.read_csv('masterdata.csv', encoding='utf-8', index_col = 0)
    except FileNotFoundError: #if no file exists yet, create an empty dataframe
        df = pd.DataFrame()

    my_dict = { 'Name'    : [],
                'Day'     : [],
                'Date'    :[],
                'check_in_time'     : [],
                'check_out_time'    :[]
              }


    name = my_entry.get()
    print(name)
    day=my_entry2.get()
    print(day)
    date=my_entry3.get()
    print(date)
    datein=my_entry4.get()
    print(datein)
    dateout=my_entry5.get()
    print(dateout)
    my_dict['Name'].append(name)
    my_dict['Day'].append(day)
    my_dict['Date'].append(date)
    my_dict['check_in_time'].append(datein)
    my_dict['check_out_time'].append(dateout)

    df['work_time'] = df['check_out_time'].sub(df['check_in_time'], axis = 0)

    #df=df[['Name', 'Day','Date','check_in_time',' check_out_time ','work_time','Total']]
    df = df.append(pd.DataFrame(my_dict))
    df.to_csv('masterdata.csv', encoding='utf-8', index= True)


#text box for emplyee name
my_label = tk.Label(root, text = "Employee name ")
my_label.grid(row = 0, column = 0)
my_entry = tk.Entry(root)
my_entry.grid(row = 0, column = 1)
#text box for checkintime
my_label1 = tk.Label(root, text = "day(Example: Monday) ")
my_label1.grid(row = 2, column = 0)
my_entry2 = tk.Entry(root)
my_entry2.grid(row = 2, column = 1)
#text box for checkintime
my_label2= tk.Label(root, text = "date(dd/mm/yy) ")
my_label2.grid(row = 3, column = 0)
my_entry3 = tk.Entry(root)
my_entry3.grid(row = 3, column = 1)
#text box for checkintime
my_label3= tk.Label(root, text = "checkintime(00.00, 24 hours system) ")
my_label3.grid(row = 4, column = 0)
my_entry4 = tk.Entry(root)
my_entry4.grid(row = 4, column = 1)
#text box for checkintime
my_label4= tk.Label(root, text = "check out time(00.00, 24 hours system) ")
my_label4.grid(row = 5, column = 0)
my_entry5 = tk.Entry(root)
my_entry5.grid(row = 5, column = 1)
# submit button and functions
my_button = tk.Button(root, text = "Submit", command = data)
my_button.grid(row = 7, column = 1)
def close():
   #win.destroy()
   root.quit()

my_button = tk.Button(root, text = "exit", command =close)
my_button.grid(row = 8, column = 1)


root.mainloop()

