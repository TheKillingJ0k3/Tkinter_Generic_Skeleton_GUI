#! python3

# Tkinter GUI Generic Skeleton by George Patoulis

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from openpyxl import *
import os, shutil


#GLOBAL VARIABLES
var = ''
last_name_initial_var = ''

#####################################################


# how functions work: I create button/widget with command=function and I put it on the grid
##################################  FUNCTIONS  ##################################################

#creates  folder inside wd, if it doesn't already exist
def createFolder(path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except OSError:
        print('Error creating directory' + path)

######################################################

def function():
    pass

def function1():
    pass

def save_variable(): #saves var when input button is pressed
    global last_name_initial_var
    last_name_initial_var = last_name_entry_initial.get()
    print (last_name_initial_var)
# as an example, this function is used in last_name_initial_submit
# when user writes last name and presses submit, script prints var's value

#############################################################################################


###################### main GUI - Button creation #########################################

root = Tk()
root.title('GUI App')
# root.state('zoomed')
# root.option_add('*tear0ff', False) #opens fullscreen

frame = Frame(root, borderwidth=5, relief="sunken", width=1000, height=20)
frame.pack()

#first line/initial/titles
initial = Label(frame, text='INITIAL', bg='gray')
initial.pack()

ID_initial = Label(frame, text='ID', bg='yellow')
last_name_initial = Label(frame, text='LAST NAME', bg='yellow')
first_name_initial = Label(frame, text='FIRST NAME', bg='yellow')
hours_initial = Label(frame, text='HOURS', bg='yellow')
start_initial = Label(frame, text='START', bg='yellow')
end_initial = Label(frame, text='END', bg='yellow')
break_time_initial = Label(frame, text='BREAK', bg='yellow')
workdays_initial = Label(frame, text='WORKDAYS', bg='yellow')
#second line/initial


#third line/initial/entries
ID_entry_initial = Entry(frame)
ID_initial_submit = Button(frame, text='Submit', command=function) 
last_name_entry_initial = Entry(frame, width='22')
last_name_initial_submit = Button(frame, text='Submit', command=save_variable)
first_name_entry_initial = Entry(frame)
first_name_initial_submit = Button(frame, text='Submit', command=function)
hours_entry_initial = ttk.Combobox(frame, width='10', textvariable=var)
hours_entry_initial['values'] = ("20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40")
hours_entry_initial.current(20)
hours_entry_initial.bind('<<ComboboxSelected>>', var)

# start_entry_initial = Entry(frame)
frame_start_initial = Frame(frame, borderwidth=4, width=120, relief="sunken", height=25)
start_entry_initial = Entry(frame)
start_hours_entry_initial = ttk.Combobox(frame_start_initial, width='2')
start_hours_entry_initial['values'] = ('00', "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", '11', "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
start_hours_entry_initial.current(0)
start_hours_entry_initial.bind('<<ComboboxSelected>>', function)
start_hours_entry_initial.pack(side=LEFT)
to_initial_start = Label(frame_start_initial, text=':', anchor='center')
to_initial_start.pack(side=LEFT)
start_minutes_entry_initial = ttk.Combobox(frame_start_initial, width='2')
start_minutes_entry_initial['values'] = ('00', "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", '55')
start_minutes_entry_initial.current(0)
start_minutes_entry_initial.bind('<<ComboboxSelected>>', function)
start_minutes_entry_initial.pack(side=LEFT)

# end_entry_initial = Entry(frame)
frame_end_initial = Frame(frame, borderwidth=4, width=120, relief="sunken", height=25)
end_entry_initial = Entry(frame)
end_hours_entry_initial = ttk.Combobox(frame_end_initial, width='2')
end_hours_entry_initial['values'] = ('00', "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", '11', "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
end_hours_entry_initial.current(0)
end_hours_entry_initial.bind('<<ComboboxSelected>>', function)
end_hours_entry_initial.pack(side=LEFT)
to_initial_end = Label(frame_end_initial, text=':', anchor='center')
to_initial_end.pack(side=LEFT)
end_minutes_entry_initial = ttk.Combobox(frame_end_initial, width='2')
end_minutes_entry_initial['values'] = ('00', "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", '55')
end_minutes_entry_initial.current(0)
end_minutes_entry_initial.bind('<<ComboboxSelected>>', function)
end_minutes_entry_initial.pack(side=LEFT)

break_time_entry_initial = ttk.Combobox(frame, width='10')
break_time_entry_initial['values'] = ('30', '40')
break_time_entry_initial.current(0)
break_time_entry_initial.bind('<<ComboboxSelected>>', function)


#initial workdays checkbuttons
workdays_frame_initial = Frame(frame)
Monday_initial_button_var = StringVar() #if booleanvar -> unchecked!!!!
Tuesday_initial_button_var = StringVar()
Wednesday_initial_button_var = StringVar()
Thursday_initial_button_var = StringVar()
Friday_initial_button_var = StringVar()
Saturday_initial_button_var = StringVar()
Sunday_initial_button_var = StringVar()
monday_initial = Checkbutton(workdays_frame_initial, text='M', variable=Monday_initial_button_var, command=var).pack(side='left')
tuesday_initial = Checkbutton(workdays_frame_initial, text='T', variable=Tuesday_initial_button_var, command=var).pack(side='left')
wednesday_initial = Checkbutton(workdays_frame_initial, text='W', variable=Wednesday_initial_button_var, command=var).pack(side='left')
thursday_initial = Checkbutton(workdays_frame_initial, text='T', variable=Thursday_initial_button_var, command=var).pack(side='left')
friday_initial = Checkbutton(workdays_frame_initial, text='F', variable=Friday_initial_button_var, command=var).pack(side='left')
saturday_initial = Checkbutton(workdays_frame_initial, text='S', variable=Saturday_initial_button_var, command=var).pack(side='left')
sunday_initial = Checkbutton(workdays_frame_initial, text='S', variable=Sunday_initial_button_var, command=var).pack(side='left')


#########################      grid     ###################################################
frame.grid(column=0, row=0)
#initial grid configuration
frame.grid(column=0, row=0, columnspan=16, rowspan=1)
#grid for first line/initial
initial.grid(column=0, row=2, columnspan=16, rowspan=1, sticky=(W))
ID_initial.grid(column=0, row=3, columnspan=1, rowspan=1, sticky=(W))
last_name_initial.grid(column=1, row=3, columnspan=1, rowspan=1, sticky=(W))
first_name_initial.grid(column=2, row=3, columnspan=1, rowspan=1, sticky=(W))
hours_initial.grid(column=3, row=3, columnspan=1, rowspan=1, sticky=(W))
start_initial.grid(column=4, row=3, columnspan=1, rowspan=1, sticky=(W))
end_initial.grid(column=5, row=3, columnspan=1, rowspan=1, sticky=(W))
break_time_initial.grid(column=6, row=3, columnspan=1, rowspan=1, sticky=(W))
workdays_initial.grid(column=10, row=3, columnspan=1, rowspan=1, sticky=(E))
#grid for second line/initial

#grid for third line/initial
ID_entry_initial.grid(column=0, row=6, columnspan=1, rowspan=1, sticky=(W))
ID_initial_submit.grid(column=0, row=6, columnspan=1, rowspan=1, sticky=(E))
last_name_entry_initial.grid(column=1, row=6, columnspan=1, rowspan=1, sticky=(W))
last_name_initial_submit.grid(column=1, row=6, columnspan=1, rowspan=1, sticky=(E))
first_name_entry_initial.grid(column=2, row=6, columnspan=1, rowspan=1, sticky=(W))
first_name_initial_submit.grid(column=2, row=6, columnspan=1, rowspan=1, sticky=(E))
hours_entry_initial.grid(column=3, row=6, columnspan=1, rowspan=1, sticky=(W))

frame_start_initial.grid(column=4, row=6, columnspan=1, rowspan=1, sticky=(NSEW))
frame_end_initial.grid(column=5, row=6, columnspan=1, rowspan=1, sticky=(NSEW))

break_time_entry_initial.grid(column=6, row=6, columnspan=1, rowspan=1, sticky=(W))

workdays_frame_initial.grid(column=10, row=6, columnspan=1, rowspan=1, sticky=(W))

######################################################################################


##############################   MENU  #############################################
menubar = Menu(root) #creates menubar
root.config(menu = menubar) #same as frame['menu'] = menubar, doesn't need menu=menu_file etc inside cascade

#creating submenus in frame menu/menubar
menu_app = Menu(menubar, tearoff=False) #initialises new submenu
menubar.add_cascade(label='New', menu=menu_app) #creates name of new submenu
menubar.add_cascade(label='Save', command=function) #adds option to submenu
# menu_app.add_command(label='Save app', command=save_excel) #adds option to submenu

# menu_app.add_command(label='Generate Random Test', command=importapp) #adds option to submenu


menu_exit = Menu(menubar)
menubar.add_cascade(label='Exit', command=frame.quit)
######################################################################################

root.mainloop()
