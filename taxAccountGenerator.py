###########################################################################
#   Program generates bank account number to pay personal taxes in Poland.
#   Copyright (C) 2025  Grzegorz Szczodrzec

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed WITHOUT ANY WARRANTY see accompanying
#   README files for details.
#
############################################################################

import tkinter as tk

#__________________________________________
def quit_app(event):
    quit()

#__________________________________________    
# pesel is incorrect
def badPesel():
    listbox.delete(0)
    listbox.insert(0,"")
    error_label.config(text = "Niepoprawny numer PESEL",fg="red")

#__________________________________________    
# chech if pesel is valid. Returns 1 on success 0 on failure
def checkPesel(peselStr):
    # check the length
    if len(peselStr) != 11:
        badPesel()
        return 0

    # only figures 
    for i in range(0,len(peselStr)):
        if peselStr[i] < '0' or peselStr[i] > '9':
            badPesel()
            return 0

    # TODO: more sophisticated checks 

    return 1    

#__________________________________________    
# Function to generate account number
# pesel is already checked to be valid
# this is the real algorithm
def generateTaxAccountNumber(peselStr):

    accountStr = "101000712221" + peselStr +"0"
    
    lk = 98 - int(accountStr + "252100")%97

    length = len(accountStr)
    result = ""
    for i in range (length,0,-1):
        pos = i - 1;
        result = str(accountStr[pos]) + result
        if pos%4 == 0:
            result = " " + result
        
    result = str(lk)  + result
    
    return result

#__________________________________________    
# Function to manage finding account number, check validity of data,
# calls real generator and so on
def calculateTaxAccountNumber(event=0):

    peselStr = pesel_entry.get()
    if checkPesel(peselStr) == 0:
        return

    accountNumberStr = generateTaxAccountNumber(peselStr)

    # clear error message (if any)
    listbox.delete(0)
    listbox.insert(0,accountNumberStr)
    error_label.config(text = "")

    #write result to the clipboard
    window.clipboard_clear()
    window.clipboard_append(accountNumberStr)
    window.update()
    
#__________________________________________    
def clear_input_fields(event):
    pesel_entry.delete(0, tk.END)
    listbox.delete(0)
    listbox.insert(0,"")
    error_label.config(text = "")

#__________________________________________
# Creating the main window
window = tk.Tk()
window.title("Generator Mikrorachunku")
window.geometry("300x180")

# Creating labels and entry fields for the variables
tk.Label(window, text="PESEL").pack()
pesel_entry = tk.Entry(window,width=11)
pesel_entry.focus_set()
pesel_entry.pack(pady=5)

# Error label
error_label = tk.Label(window, text="")
error_label.pack(pady=10)

# display results
listbox=tk.Listbox(window, height=1,width=29)
listbox.insert(0,"")
listbox.pack()

# Quit program
quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack(pady=10)


# keybinding to make fast actions
window.bind('<Escape>', clear_input_fields)
window.bind('<Control-q>',quit_app)
window.bind('<Return>', calculateTaxAccountNumber)

# Run the application
window.mainloop()


