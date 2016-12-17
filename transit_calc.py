#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 16 Dec 2016
# TODO Add natural language capability to date entry field - e.g. today, tomorrow, Friday

from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta


def calc():
    # Defines transit time dependant on which method radio button id selected.
    if method.get() == 'Sea':
        transitTime = 42
        msg = ttk.Label(text='TEST: SEA FREIGHT: {}'.format(transitTime))
        msg.grid(row=7)

    elif method.get() == 'Air':
        transitTime = 10
        msg = ttk.Label(text='TEST: AIR FREIGHT: {}'.format(transitTime))
        msg.grid(row=7)
    else:
        msg = ttk.Label(text='TEST: MISSING METHOD: ERROR')
        msg.grid(row=7)

    dateEntered = datetime.strptime(entry.get(), '%d/%m/%Y')
    rawDue = dateEntered + timedelta(days=transitTime)
    #tempDue = ttk.Label(text='test date: {}'.format(rawDue))
    #tempDue.grid(row=8)

    # Checks the weekday number of rawDue and round up to next Friday.
    weekday = (rawDue.weekday())

    if weekday == 0:
        due = rawDue + timedelta(days=4)
    elif weekday == 1:
        due = rawDue + timedelta(days=3)
    elif weekday == 2:
        due = rawDue + timedelta(days=2)
    elif weekday == 3:
        due = rawDue + timedelta(days=1)
    elif weekday == 4:
        due = rawDue + timedelta(days=0)
    elif weekday == 5:
        due = rawDue + timedelta(days=-1)
    elif weekday == 6:
        due = rawDue + timedelta(days=-2)
    else:
        TypeError("Possible Error: Unrecognised Week Day")

    arrive = ttk.Label(root, text='Estimated Arrival Date: {}'.format(due))
    arrive.grid(row=6)

root = Tk()
title = ttk.Label(text='ISM Transit Time Calculator', font=('verdana', 14, 'bold'))
title.grid(row=0, columnspan=3)
subhead1 = ttk.Label(text='Select Shipping Method...')
subhead1.grid(row=1, column=0)

method = StringVar()
Sea = ttk.Radiobutton(root, text='Sea', variable=method, value='Sea')
Sea.grid(row=1, column=1)
Air = ttk.Radiobutton(root, text='Air', variable=method, value='Air')
Air.grid(row=1, column=2)


subhead2 = ttk.Label(root, text='Enter ship date (DD/MM/YYYY)...')
subhead2.grid(row=2, column=0)
entry = ttk.Entry(root, width=10)
entry.grid(row=2, column=1)


calculate = ttk.Button(root, text='Calculate', command=calc)
calculate.grid(row=2, column=3)
# TODO: If no Radiobutton is selected then calculate button should be disalbled.


root.mainloop()
