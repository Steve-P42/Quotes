# Welcome to the real world, I hope you'll enjoy it!
# author: Steve-P42
# creation date: 2021-02-15 08:29:45
# purpose: Display a random quote in a simple window
# status: in progress
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
    number_of_quotes = len(quotes)
    str_quote = quotes[index]

    txtbox = Text(main_window, height=7, width=25, bg='blue', fg='black', font=('verdana', 20),
                  wrap=WORD, relief=GROOVE)
    txtbox.pack()

    txtbox.insert(END, str_quote)

    def move_quote():
        """change the quotes displayed"""
        try:
            index = int(spinbox1.get())
            str_quote = quotes[index - 1]
            txtbox.delete('1.0', END)
            txtbox.insert(END, str_quote)
        except IndexError:
            pass


    spinbox1 = Spinbox(main_window, from_=1, to=number_of_quotes, command=move_quote, bg='gray', fg='blue',
                       font=('verdana', 20), width=3)

    spinbox1.pack()

    def close_window():
        """exit function"""
        main_window.destroy()  # you could just exit without destroying window first
        exit()

    # button for exit
    button1 = Button(main_window, text="Exit", width=5, command=close_window)
    button1.pack()

    mainloop()


main()

# %%
# %%
# %%
# %%
# %%