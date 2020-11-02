from tkinter import *
from os import startfile
import pandas as pd
from add_vocab import AddVocab
from quiz import Quiz
from datetime import datetime


window = Tk()

window.title("Vocabulary Trainer")
window.geometry('303x190')


def clicked_practice():
    Quiz()

def clicked_add():
    AddVocab()

def clicked_excel():
    dt_string = datetime.now().strftime("%d_%m_%Y %H-%M-%S")
    filename = 'Vocabulary {}.xlsx'.format(dt_string)
    vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
    vocab_table.to_excel(filename)
    startfile(filename)


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
