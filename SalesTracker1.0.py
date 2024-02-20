##############################################################
#This is a sale tracking app that allows the
#user to enter data about their product and customers
#for tracking sales and user information and outputs 
#it in an excel file
##############################################################

import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl                       #this will import the excel packages
import datetime                       #this will import a date widget
from openpyxl import Workbook
from tkcalendar import DateEntry      #this will import the calender module
import customtkinter as ctk           #imports theme  
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font


##########################################################
# this function gets executed when the user presses
# the "Enter Data button" and writes it
# to an excell file
##########################################################

def enter_data():
    date = date_sold_entry.get()
    product = product_type_combobox.get()
    qt = int(quantity_needed_entry.get()) 
    sw_price = int(price_of_sweater_entry.get())
    sh_price = int(shipping_of_sweater_entry.get())
    filepath = "C:\\Users\julie\OneDrive\Desktop\Babaco\Little babaco sales tracker.xlsx"
    workbook = openpyxl.load_workbook(filepath)                #this opens the excell document
    sheet = workbook.active                                    #this opens the active sheet
    sheet.append([date, product ,qt, sw_price, sh_price])      #finds the active sheet and appends the data
    workbook.save(filepath)
    
##################################################################################
window = tkinter.Tk()                                   # main window created
window.title("Little Babaco - Sales Entry Form")        # main window title

#Selling information frame
frame = tkinter.Frame(window)                           #putting a frame inside the main window
frame.pack()                                            #packing is positioning the frame in the window, facilitates resizing

#customer information frame
customer_information = tkinter.LabelFrame(frame, text= "Customer Information", pady= 10)
customer_information.grid(row=0, column=0)              #positioning the labelframe in position 0 x 0

#calendar of date sold label
date_sold = tkinter.Label(customer_information, text= "Date sold (D/M/Y):")
date_sold.grid(row=0, column=0)                         #positioning the label in position 0 x 0  
date_sold_entry = DateEntry(customer_information,selectmode='day', year=2023, month=8, day=24) #this will create a date entry calender
date_sold_entry.grid(row=1, column=0, padx=15)          

#Customer name label
name_of_customer = tkinter.Label(customer_information, text = "Customer Name:")
name_of_customer.grid(row=0, column=1)
name_of_customer_entry = tkinter.Entry(customer_information)   #entry for product type
name_of_customer_entry.grid(row=1, column=1)



#product information frame
product_information = tkinter.LabelFrame(frame, text= "Product Information", pady= 10)
product_information.grid(row=1, column=0, sticky="news")     #positioning the labelframe in position 1 x 0

#product type label
product_type = tkinter.Label(product_information, text= "Enter product type (Sweater, hat, etc...)")
product_type.grid(row=0, column=0)
product_type_combobox = ttk.Combobox(product_information, values= ["sweater", "hat", "beanie", "brush", "bracelet"])
#product_type_entry = tkinter.Entry(product_information)
#product_type_entry.grid(row=1, column=0)
product_type_combobox.grid(row=1, column=0)



#quantity frame, paid/not paid etc frame
quantity = tkinter.LabelFrame(frame, text = "Quantity", pady= 10)
quantity.grid(row=2, column=0)

#Quantity label
quantity_needed = tkinter.Label(quantity, text="Enter quantity:")
quantity_needed.grid(row=0, column=0)
quantity_needed_entry = tkinter.Spinbox(quantity, from_= 1, to=100)
quantity_needed_entry.grid(row=1, column=0)

#paid or not paid label
paid_not_paid = tkinter.Label(quantity, text= "Has the user paid or not")
paid_not_paid_check = tkinter.Checkbutton(quantity)
paid_not_paid.grid(row=0, column=1)
paid_not_paid_check.grid(row=1, column=1)


#pricing Frame
pricing = tkinter.LabelFrame(frame, text= "Pricing")
pricing.grid(row=3, column=0, sticky="news")

#price of sweater label
price_of_sweater = tkinter.Label(pricing, text = "Enter price of sweater")
price_of_sweater.grid(row=0, column=0)
price_of_sweater_entry = tkinter.Entry(pricing)
price_of_sweater_entry.grid(row=1, column=0)

#shipping coast label
shipping_of_sweater = tkinter.Label(pricing, text = "Shipping Price")
shipping_of_sweater.grid(row=0, column=1)
shipping_of_sweater_entry = tkinter.Entry(pricing)
shipping_of_sweater_entry.grid(row=1, column=1)

#Enter data button
button = tkinter.Button(frame, text = "Enter Data", pady=10, command= enter_data)
button.grid(row=4, column=0, pady=10)


for widget in customer_information.winfo_children():   #these 4 for loop takes all the grid functions and add
    widget.grid_configure(padx=10, pady=5)             # padding on each axis (x and y)

for widget in product_information.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in product_type.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in quantity.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in pricing.winfo_children():
    widget.grid_configure(padx=10, pady=5)



window.mainloop()

