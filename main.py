##############################################################
#This is a sale tracking app that allows the
#user to enter data about their product and customers
##############################################################



import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl

window = tkinter.Tk()  # main window create
window.title("Little Babaco - Sales Entry Form") # main window title

frame = tkinter.Frame(window)                        #putting a frame inside the main window
frame.pack()                                         #packing is positioning the frame in the window, facilitates resizing

#Saving User Info
customer_information = tkinter.LabelFrame(frame, text= "Customer/Product Information")
customer_information.grid(row=0, column=0)           #positioning the labelframe in position 0 x 0

date_sold = tkinter.Label(customer_information, text="Date sold (D/M/Y)")
date_sold.grid(row=1, column=0)                     #positioning the label in position 0 x 0
date_sold_entry = tkinter.Entry(date_sold)          #entry for date product was sold
date_sold_entry.grid(row=1, column=0)

product = tkinter.Label(customer_information, text = "Product type")
product.grid(row=1, column=1)
product_entry = tkinter.Entry(product)              #entry for product type
product_entry.grid(row=1, column=1)

window.mainloop()