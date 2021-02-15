# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# My Glossary Project
# video source: https://www.youtube.com/watch?v=_lSNIrR1nZU
# video name:   Learn Tkinter in 20 Minutes

# (https://www.youtube.com/watch?v=P6azEyNIQDQ create a menu in python)


import tkinter as tk
from sys import exit


# key down function
def click():
    entered_text = textentry.get()  # get text from entry box
    output.delete(0.0, tk.END)
    try:
        characteristics = charDict[entered_text]
    except:
        characteristics = "No data available. Try different request."

    output.insert(tk.END, characteristics)


# exit function
def close_window():
    window.destroy()  # you could just exit without destroying window first
    exit()


# ## main:
window = tk.Tk()
window.title("Red Pill or Blue Pill?")
window.configure(background="black")

# ## my photo
photo1 = tk.PhotoImage(file="morpheus.gif")
tk.Label(window, image=photo1, bg="black").grid(row=0, column=0)

# create a label
tk.Label(window, text="Enter character you want information about:",
         bg="black", fg="green", font="none 12 bold").grid(row=1, column=0)

# create a textbox
textentry = tk.Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0)

# submit button
tk.Button(window, text="ENTER", width=5, command=click).grid(row=3, column=0)

# create another label
tk.Label(window, text="\nCharacteristics:", bg="black", fg="green",
         font="none 12 bold").grid(row=4, column=0)

# output box
output = tk.Text(window, width=75, height=6, background="#000000", fg="green")
output.grid(row=5, column=0, columnspan=2)

# build a dictionary
charDict = {'Neo': 'The Chosen One. The One. The Action Principle of the Brain.',
            'Trinity': 'The unifying force. The connection with the heart.',
            'Morpheus': 'The Roman god of sleep. He awakens the One. He shows the light and the path.'
            }

# exit button
tk.Label(window, text="click to exit program", bg="black", fg="green",
         font="none 12 bold").grid(row=6, column=0)
# button for exit
tk.Button(window, text="Exit", width=5, command=close_window).grid(row=7, column=0)

# ## runs the main loop
window.mainloop()
