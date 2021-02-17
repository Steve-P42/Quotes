# Welcome to the real world, I hope you'll enjoy it!
# author: Steve-P42
# creation date: 2021-02-15 08:29:45
# purpose: Display a random stoic quote in a simple window
# status: in progress
# %%
from tkinter import *
from tkinter.ttk import *
import re
from random import randint


def main():
    """the main function that contains the tkinter window loop"""
    # initialize window manager
    main_window = Tk()
    # rename the title of your window
    main_window.title('Stoic Quotes')
    # configure window appearance
    main_window.configure(bg="black")
    # change window size > set to new geometry "widthxheight+x+y
    main_window.geometry("900x442+800+300")  # dimension and positioning on screen
    # lock size
    main_window.resizable(height=0, width=0)

    # extracting quotes from a txt file:
    stoic_quotes_content = open("stoic_quotes.txt", "r", encoding='utf8')
    stoic_quotes_content_txt = stoic_quotes_content.read()

    distinct_quotes = re.split("\n\n", stoic_quotes_content_txt)

    stoic_quotes_content.close()

    # picking random quote
    index = randint(1, len(distinct_quotes) - 1)

    picked_quote = distinct_quotes[index]

    # text widget
    textbox = Text(main_window, height=14, width=55, bg='blue', fg='black', font=('verdana', 18),
                   wrap=WORD, relief=FLAT)
    textbox.pack()

    # putting text into the textbox:
    textbox.insert(END, picked_quote)

    def get_new_quote():
        """change the quotes displayed"""
        new_quote = distinct_quotes[randint(1, len(distinct_quotes) - 1)]
        textbox.delete('1.0', END)
        textbox.insert(END, new_quote)

    # Create style Object
    style = Style()

    # Add style to every available button
    style.configure('TButton', font=('verdana', 10, 'bold', 'underline'), foreground='blue')

    # random button
    button1 = Button(main_window, text="Random Quote", width=20, command=get_new_quote)
    button1.pack()

    mainloop()


main()

# %% finding the longest quote:
# import re
#
# stoic_quotes_content = open("stoic_quotes.txt", "r", encoding='utf8')
# stoic_quotes_content_txt = stoic_quotes_content.read()
#
# distinct_quotes = re.split("\n\n", stoic_quotes_content_txt)
#
# stoic_quotes_content.close()
#
# arr = []
# for i in distinct_quotes:
#     arr.append([len(i), i])
#
# print(max(arr))

# longest quote:
# picked_quote = 'There are times when even to live is an act of bravery. So there is the comforting thing about\
# extremities of pain: if you feel it too much you are bound to stop feeling it. The love of power or money or\
# luxurious living are not the only things which are guided by popular thinking. We take our cue from people’s\
# thinking even in the way we feel pain. Another thing which will help you is to turn your mind to other thoughts\
# and that way get away from your suffering. Call to mind things which you have done that have been upright or\
# courageous; run over in your mind the finest parts you have played. ‘But my illness has taken me away from my\
# duties and won’t allow me to achieve anything.’ It is your body, not your mind as well, that is in the grip of\
# ill health.\nSeneca\nLetter LXXVIII'

# %%
# %% csv version with spinbox:
#
# from tkinter import *
# import csv
#
#
# def main():
#     """the main function that contains the tkinter window loop"""
#     # initialize window manager
#     main_window = Tk()
#     # rename the title of your window
#     main_window.title('Quotes')
#     # configure window appearance
#     main_window.configure(bg="black")
#     # change window size > set to new geometry "widthxheight+x+y
#     main_window.geometry("500x350+800+300")  # dimension and positioning on screen
#
#     # quotes list
#     quotes = []
#     # extracting quotes from a csv file with delimiter ';' :
#     with open("quotes.csv", "r") as fin:
#         myreader = csv.reader(fin, delimiter=";")
#         for row in myreader:
#             quotes.append(row[0])
#
#     index = 0
#     number_of_quotes = len(quotes)
#     str_quote = quotes[index]
#
#     txtbox = Text(main_window, height=7, width=25, bg='blue', fg='black', font=('verdana', 20),
#                   wrap=WORD, relief=GROOVE)
#     txtbox.pack()
#
#     # putting text into the textbox:
#     txtbox.insert(END, str_quote)
#
#     def move_quote():
#         """change the quotes displayed"""
#         try:
#             index = int(spinbox1.get())
#             str_quote = quotes[index - 1]
#             txtbox.delete('1.0', END)
#             txtbox.insert(END, str_quote)
#         except IndexError:
#             pass
#
#     # this widget lets us pick a quote by clicking the arrows with the mouse
#     spinbox1 = Spinbox(main_window, from_=1, to=number_of_quotes, command=move_quote, bg='gray', fg='blue',
#                        font=('verdana', 20), width=3)
#
#     spinbox1.pack()
#
#     def close_window():
#         """exit function"""
#         main_window.destroy()  # you could just exit without destroying window first
#         exit()
#
#     # exit button
#     button1 = Button(main_window, text="Exit", width=5, command=close_window)
#     button1.pack()
#
#     mainloop()
#
#
# main()

# %%
# %%
# %%
# %%
# %%
