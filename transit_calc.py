#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 19 Dec 2016
# Revision 3 of ISM Transit Time Calculator

from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
import calendar

#-------------------------------------------------------------------
# Variables:
#-------------------------------------------------------------------
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
thirty_one = ('Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec')
thirty = ('Apr', 'Jun', 'Sep', 'Nov')
temp_date_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
year_range  = (2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025)
today = datetime.now()
current_yyyy = datetime.strftime(today, '%Y')
current_mm = datetime.strftime(today, '%b')
current_dd = datetime.strftime(today, '%d')

#-------------------------------------------------------------------
# Functions:
#-------------------------------------------------------------------
def method(): # Takes input from transit method radiobuttons to assign a transit time to 'transit' var.
    global transit
    if method.get() == 'sea':
        transit = 42
    elif method.get() == 'air':
        transit = 10
    else: TypeError('Unknown Transit Method. Please select from Sea or Air')
    return transit

def set_picker(): # Sets the date picker comboboxes each time a ship date radiobutton is clicked.
    #TODO If today then do one thing, if tomorrow do x if etc...
    #TODO Work out how to deal with tomorrow or Friday where a new month or year will have started.
    yr_select.set(current_yyyy)
    mth_select.set(current_mm)
    if ship_pick.get() == 'today':
        day_select.set(current_dd)
    elif ship_pick.get() == 'tomorrow':
        day_select.set(int(current_dd) + 1)
    elif ship_pick.get() == 'nxt_friday':
        day_select.set(int(current_dd) + friday(datetime.now()))
    elif ship_pick.get() == 'select':
        pass
    else: TypeError('Please make a valid ship date selection!')

def friday(in_date):
    weekday = in_date.weekday()
    global time_shift
    time_shift = ''
    if weekday == 0:
        time_shift = 4
    elif weekday == 1:
        time_shift = 3
    elif weekday == 2:
        time_shift = 2
    elif weekday == 3:
        time_shift = 1
    elif weekday == 4:
        time_shift = 0
    elif weekday == 5:
        time_shift = -1
    elif weekday == 6:
        time_shift = -2
    else:
        TypeError("Possible Error: Unrecognised Week Day")
    return time_shift

def ship():
    #TODO Create a variable from ship pickers VALUES and the calc from that. This func could then be removed.
    global ship_date
    ship_date = None
    if ship_pick.get() == 'today':
        ship_date = today
    elif ship_pick.get() == 'tomorrow':
        ship_date = today + timedelta(days=1)
    elif ship_pick.get() == 'nxt_friday':
        ship_date = today + timedelta(days=time_shift)
    elif ship_pick.get() == 'select':
        ship_date = today
    else: TypeError('ERROR: TBC')
    return ship_date


def calc():
    global expected
    expected = ship() + timedelta(days=10)
    return expected



#-------------------------------------------------------------------
# Interface
#-------------------------------------------------------------------
root = Tk()

# Title
title = ttk.Label(root, text='ISM Transit Time Calculator', font=('verdana', 16, 'bold'))
title.grid(row=0, columnspan=5)

# Select transport method. method() will take this input to define the transit time.
subhead1 = ttk.Label(root, text='Select Shipping Method:', font=('verdana', 10, 'bold'))
subhead1.grid(row=1, column=0)
method = StringVar()
sea = ttk.Radiobutton(root, text='Sea', variable=method, value='sea')
sea.grid(row=1, column=1)
air = ttk.Radiobutton(root, text='Air', variable=method, value='air')
air.grid(row=1, column=2)
# TEST


# Select ship date. ship_date() will take input and define ship variable or activate picker.
subhead2 = ttk.Label(root, text='Select Ship Date: ', font=('verdana', 10, 'bold'))
subhead2.grid(row=2, column=0)
ship_pick = StringVar()
today = ttk.Radiobutton(root, text='Today', variable=ship_pick, value='today')
today.grid(row=2, column=1)
today.config(command=set_picker)
today.invoke()
tomorrow = ttk.Radiobutton(root, text='Tomorrow', variable=ship_pick, value='tomorrow')
tomorrow.grid(row=2, column=2)
tomorrow.config(command=set_picker)
nxt_friday = ttk.Radiobutton(root, text='Friday', variable=ship_pick, value='nxt_friday')
nxt_friday.grid(row=2, column=3)
nxt_friday.config(command=set_picker)
select = ttk.Radiobutton(root, text='Enter a Date', variable=ship_pick, value='select')
select.grid(row=2, column=4)

# Date Picker
subhead3 = ttk.Label(root, text='Pick Date: ', font=('verdana', 10, 'bold'))
subhead3.grid(row=3, column=0)
yr = StringVar()
yr_select = ttk.Combobox(root, textvariable=yr)
yr_select.grid(row=3, column=1)
yr_select.config(values=year_range, width=5)

mth = StringVar()
mth_select = ttk.Combobox(root, textvariable=mth)
mth_select.grid(row=3, column=2)
mth_select.config(values=months, width=5)

day = StringVar()
day_select = ttk.Combobox(root, textvariable=day)
day_select.grid(row=3, column=3)
day_select.config(values=temp_date_range, width=5)

set_picker()

# Calculate
calc_but = ttk.Button(root, text='Calculate')
calc_but.grid(row=4, column=4)
#calc_but.config(command=calc(ship_date))
subhead4 = ttk.Label(root, text='Expected Arrival:', font=('verdana', 10, 'bold'))
subhead4.grid(row=5, column=0)
result = ttk.Label(root, text=calc(), font=('verdana', 10, 'bold'))
result.grid(row=5, column=1)


# Status Bar
status = ttk.Label(root, text='Today is {}/{}/{}'.format(current_dd, current_mm, current_yyyy))
status.grid(row=7, columnspan=5)
status.config(background='#97f09b', width=50)

root.mainloop()