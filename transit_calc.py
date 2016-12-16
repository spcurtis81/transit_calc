#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 16 Dec 2016


from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta


def calc():
    ship = datetime.now()
    air = 10
    sea = 42




root = Tk()
title = ttk.Label(text='Transit Time Calculator', font=('verdana', 14, 'bold')).pack()
subhead1 = ttk.Label(text='Select Shipping Method...').pack()


method = StringVar()
ttk.Radiobutton(root, text='Sea', variable=method, value='Sea').pack()
ttk.Radiobutton(root, text='Air', variable=method, value='Air').pack()
# If no button is selected, raise error.

calculate = ttk.Button(text='Calculate').pack()
arrive = ttk.Label(text='Estimated Arrival Date: ').pack()

root.mainloop()
