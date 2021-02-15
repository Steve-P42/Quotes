# Welcome to the real world, I hope you'll enjoy it!
# author: Steve-P42
# creation date: 2021-02-15 08:29:45
# purpose: Display a random quote in a simple window
# status:
# %%

# %%

# %%

# %%
from tkinter import *
import csv


def main():
    # initialize window manager
    main_window = Tk()
    # rename the title of your window
    main_window.title('Quotes')
    # configure window appearance
    main_window.configure(bg="black")
    # change window size > set to new geometry "widthxheight+x+y
    main_window.geometry("500x350+800+300")  # dimension and positioning on screen

    quotes = []
    with open("quotes.csv", "r") as fin:
        myreader = csv.reader(fin, delimiter=";")
        for row in myreader:
            quotes.append(row[0])

    index = 0
    str_quote = quotes[index]
    msg = Message(main_window, text=str_quote,
                  padx=25, pady=20, bd=5, relief=GROOVE)
    msg.config(bg='gray', fg='blue', font=('verdana', 25))

    msg.pack()

    def move_quote():
        index = int(spinbox1.get())
        str_quote = quotes[index - 1]
        msg.config(text=str_quote)

    spinbox1 = Spinbox(main_window, from_=1, to=5, command=move_quote, bg='gray', fg='blue', font=('verdana', 20),
                       width=5)

    spinbox1.pack(side=LEFT)

    # exit function
    def close_window():
        main_window.destroy()  # you could just exit without destroying window first
        exit()

    # exit button
    # label1 = Label(main_window, text="click to exit program", bg="black", fg="green", font="none 12 bold")
    # label1.pack(side=BOTTOM)
    # button for exit
    button1 = Button(main_window, text="Exit", width=5, command=close_window)
    button1.pack(side=RIGHT)

    mainloop()


main()
# %%

# %%

