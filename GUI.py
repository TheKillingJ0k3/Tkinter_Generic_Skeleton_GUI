#! python3

# Tkinter GUI Generic Skeleton by George Patoulis

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from openpyxl import *
import os, shutil


#GLOBAL VARIABLES
var = ''

#####################################################


#pws leitourgoun ta functions: ftiaxnw button/widget me command=function kai to vazw sto grid
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

def save_excel():
    wb.save(".\\Shift Change Files\\{}.xlsx".format(var))
    messagebox.showinfo('Alert!', 'File saved!')


#############################################################################################

############################ EXCEL ############################
createFolder('.\\Shift Change Files')
wb = load_workbook('.\\Documents\\Python Exercises\\folder\\Excel.xlsx')
ws = wb.active
ws['D5'] = var + 'string'

###################### main GUI - Button creation #########################################

root = Tk()
root.title('App')
root.state('zoomed')
root.option_add('*tear0ff', False) #opens fullscreen

#frame
frame = Frame(root, borderwidth=5, relief="sunken", width=1000, height=20)
frame.pack()
#label
label = Label(frame, text='string', bg='gray')
label.pack()
#label in frame
frame2 = Frame(frame, borderwidth=5, relief="sunken", width=1000, height=20)
date = Label(frame2, text="Date: ")
date.pack()
#buttons
date_initial_date1 =  Button(frame, text='str', command=function1)
to_initial = Label(frame, text='-', anchor='center')
date_initial_date2 =  Button(frame, text='str', command=function)
#combobox
hours_entry_initial = ttk.Combobox(frame, width='10', textvariable=var)
hours_entry_initial['values'] = ("20", "21", "22", "23", "24", "25")
hours_entry_initial.current(20)
hours_entry_initial.bind('<<ComboboxSelected>>', function)
#entry
entry = Entry(frame)
#checkbuttons in frame
workdays_frame_initial = Frame(frame)
Monday_initial_button_var = StringVar() #if booleanvar -> unchecked!!!!
Tuesday_initial_button_var = StringVar()
Wednesday_initial_button_var = StringVar()
Thursday_initial_button_var = StringVar()
Friday_initial_button_var = StringVar()
Saturday_initial_button_var = StringVar()
Sunday_initial_button_var = StringVar()
monday_initial = Checkbutton(workdays_frame_initial, text='M', variable=Monday_initial_button_var, command=check_Monday_initial_var).pack(side='left')
tuesday_initial = Checkbutton(workdays_frame_initial, text='T', variable=Tuesday_initial_button_var, command=check_Tuesday_initial_var).pack(side='left')
wednesday_initial = Checkbutton(workdays_frame_initial, text='W', variable=Wednesday_initial_button_var, command=check_Wednesday_initial_var).pack(side='left')
thursday_initial = Checkbutton(workdays_frame_initial, text='T', variable=Thursday_initial_button_var, command=check_Thursday_initial_var).pack(side='left')
friday_initial = Checkbutton(workdays_frame_initial, text='F', variable=Friday_initial_button_var, command=check_Friday_initial_var).pack(side='left')
saturday_initial = Checkbutton(workdays_frame_initial, text='S', variable=Saturday_initial_button_var, command=check_Saturday_initial_var).pack(side='left')
sunday_initial = Checkbutton(workdays_frame_initial, text='S', variable=Sunday_initial_button_var, command=check_Sunday_initial_var).pack(side='left')


#########################      grid     ###################################################
frame.grid(column=0, row=0)
#initial grid configuration
frame.grid(column=0, row=0, columnspan=16, rowspan=1)
#grid for first line/initial
frame2.grid(column=0, row=2, columnspan=16, rowspan=1, sticky=(W))
hours_entry_initial.grid(column=0, row=3, columnspan=1, rowspan=1, sticky=(W))
workdays_frame_initial.grid(column=1, row=3, columnspan=1, rowspan=1, sticky=(W))


######################################################################################


##############################   MENU  #############################################
menubar = Menu(root) #creates menubar
root.config(menu = menubar) #same as frame['menu'] = menubar, doesn't need menu=menu_file etc inside cascade

#creating submenus in frame menu/menubar
menu_shift_change = Menu(menubar, tearoff=False) #initialises new submenu
menubar.add_cascade(label='New Shift Change', menu=menu_shift_change) #creates name of new submenu
menubar.add_cascade(label='Save Changes', command=save_excel) #adds option to submenu
# menu_shift_change.add_command(label='Save shift_change', command=save_excel) #adds option to submenu

# menu_shift_change.add_command(label='Generate Random Test', command=importshift_change) #adds option to submenu


menu_exit = Menu(menubar)
menubar.add_cascade(label='Exit', command=frame.quit)
######################################################################################

root.mainloop()
