from tkinter import ttk
import tkinter as tk

my_w = tk.Tk()
my_w.geometry("560x280")
my_w.title("Title")

import csv
file=open('students.csv')
csvreader=csv.reader(file)
l1=[]
l1=next(csvreader)
r_set=[row for row in csvreader] #list of rows of data


# print(l1)
# print(r_set)

trv=ttk.Treeview(my_w, selectmode='browse')
trv.grid(row=1, column=1, padx=30, pady=20)
trv['height']=5
trv['show']='headings'
trv['columns']=l1
for i in l1:
    trv.column(i,width=100, anchor='c')
    trv.heading(i, text=i)
for dt in r_set:
    v=[r for r in dt]
    trv.insert('','end',iid=v[0], values=v)


my_w.mainloop() 