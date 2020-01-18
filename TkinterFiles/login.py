import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

def conacona():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS stud (firstname TEXT, secondname TEXT)")
    conn.commit()
    conn.close()

#oooooooo 

main_menu = tk.Tk()

firstname_label = Label(main_menu, text="First name")
firstname_label.pack()
secondname_label = Label(main_menu, text="Second name")
secondname_label.pack()

# First name get 
firstname_entry = tk.StringVar()
firstname_entry_entry = Entry(main_menu, textvariable=firstname_entry)
firstname_entry_entry.pack()

# Second name get 
secondname_entry = tk.StringVar()
secondname_entry_entry = Entry(main_menu, textvariable=secondname_entry)
secondname_entry_entry.pack()

def savedata ():
    # print(dir(firstname_entry))
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('INSERT INTO stud (firstname, secondname) VALUES (?,?)', (firstname_entry.get(), secondname_entry.get()))
    conn.commit()
    print("OK")

u_ent_btn = Button(text="Enter",command=savedata)
u_ent_btn.pack()

conacona()
main_menu.mainloop()