# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:21:59 2020

@author: tjfea
"""
from tkinter import *


#create window
root = Tk()
root.geometry('1000x450')



#create frames 
top_frame = Frame(root)
top_frame.pack(fill = X)
mid_frame = Frame(root)
mid_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack()
message_frame = Frame(root)
message_frame.pack()

#create window title
title_label = Label(top_frame, text = 'STOCK CALCULATOR',  bg = '#036635', fg = 'white')
title_label.config(font=('santana-black',34))
title_label.pack(fill = X)


#create grid of lables and entries
#Current stock
label_current_stock = Label(mid_frame, text = 'Number currently in stock:   ')
label_current_stock.config(font=('Arial Black',15)) 
entry_current_stock = Entry(mid_frame, font=('Ariel',12))
entry_current_stock.config(width = 5)

label_current_stock.grid(row=0, column=0,  pady=5)
entry_current_stock.grid(row=0, column=1)

#target stock
label_target_stock = Label(mid_frame, text = 'Target number in stock:   ')
label_target_stock.config(font=('Arial Black',15)) 
entry_target_stock = Entry(mid_frame, font=('Ariel',12))
entry_target_stock.config(width = 5)

label_target_stock.grid(row=1, column=0, pady=5)
entry_target_stock.grid(row=1, column=1)

#average sold
label_average_sold = Label(mid_frame, text = 'Average number sold each day:   ')
label_average_sold.config(font=('Arial Black',15)) 
entry_average_sold = Entry(mid_frame, font=('Ariel',12))
entry_average_sold.config(width = 5)

label_average_sold.grid(row=2, column=0, pady=5)
entry_average_sold.grid(row=2, column=1)

#out of date
label_out_of_date = Label(mid_frame, text = 'Number going out of date in the next two days:   ')
label_out_of_date.config(font=('Arial Black',15)) 
entry_out_of_date = Entry(mid_frame, font=('Ariel',12))
entry_out_of_date.config(width = 5)

label_out_of_date.grid(row=3, column=0, pady=5)
entry_out_of_date.grid(row=3, column=1)

#currently in irder
label_currently_ordered = Label(mid_frame, text = 'Number currently on order:   ')
label_currently_ordered.config(font=('Arial Black',15)) 
entry_currently_ordered = Entry(mid_frame, font=('Ariel',12))
entry_currently_ordered.config(width = 5)

label_currently_ordered.grid(row=4, column=0, pady=5)
entry_currently_ordered.grid(row=4, column=1)


#spacer
spacer = Label(mid_frame,text = '')
spacer.grid(row=5)


#make output  variable string
output = StringVar()

#Define function for calculation
def calculate_order():
    try:
        if 2*int(entry_average_sold.get()) > int(entry_out_of_date.get()):
            order_amount = int(entry_target_stock.get()) - (int(entry_currently_ordered.get()) + int(entry_current_stock.get()) - int(entry_average_sold.get()) *2)
        else:
            order_amount = int(entry_target_stock.get()) - (int(entry_currently_ordered.get()) +  int(entry_current_stock.get()) - int(entry_out_of_date.get()))
        if order_amount > 0:    
            output.set('Order Required:   ' + str(order_amount))
        else:
            output.set('No Order Required')
    except ValueError:
        output.set('Check all entries contain values')
        

#Define function that clears variable and output message
def reset_variables():
    
    entry_average_sold.delete(0,'end')
    entry_current_stock.delete(0,'end')
    entry_currently_ordered.delete(0,'end')
    entry_out_of_date.delete(0,'end')
    entry_target_stock.delete(0,'end')
    output.set(' ')      
    
    


#create run button and attatch to function
run_button = Button(bottom_frame, text = 'CALCULATE', bg = '#036635', fg = 'white', command = calculate_order)
run_button.config(font=('santana-black', 20))
run_button.grid(row=0)

#create reset button and attatch function
reset_button = Button(bottom_frame, text = 'RESET', command = reset_variables)
reset_button.config(font=('santana-black', 20))
reset_button.grid(row=0, column=1)


#create label for output
label_output = Label(message_frame, textvariable = output)
label_output.config(font=('Arial Black',20))
label_output.grid()



quit_button = Button(message_frame, text = 'EXIT', command = root.destroy)
quit_button.config(font=('santana-black', 15))
quit_button.grid(row=1)

root.mainloop()