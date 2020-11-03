from tkinter import *
from os import startfile
import pandas as pd
from add_vocab import AddVocab
from quiz import Quiz, NoTable
from datetime import datetime


window = Tk()

window.title("Vocab!")
window.geometry('303x190')


def clicked_practice():
    quiz = Quiz()

def clicked_add():
    AddVocab()

def clicked_excel():
    dt_string = datetime.now().strftime("%Y_%m_%d %H-%M-%S")
    filename = 'Vocab!      {}.xlsx'.format(dt_string)
    try:
        vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
        vocab_table.to_excel(filename)
        startfile(filename)
    except FileNotFoundError:
        NoTable()


btn1 = Button(window, text="Add Vocabulary", command=clicked_add)
btn1.config(height=8, width=20)
btn2 = Button(window, text="Practice", command=clicked_practice)
btn2.config(height=8, width=20)
btn3 = Button(window, text="Create Excel", command=clicked_excel)
btn3.config(height=3, width=25)

btn1.grid(column=0, row=0)
btn2.grid(column=1, row=0)
btn3.grid(column=0, row=1, columnspan=2)


window.mainloop()
