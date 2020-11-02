import pandas as pd
import os.path
from tkinter import *


# read existing .csv table or create new one
def initialize_addVocab():
    if not os.path.isfile('vocabulary.csv'):
        vocab_table = pd.DataFrame(columns=['Foreign', 'Meaning1', 'Meaning2', 'Meaning3'])
        vocab_table.to_csv('vocabulary.csv')
        print("Initializing: Could not find existing table. Created new table.\n")

    else:
        vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
        print("Initializing: Found existing table with {} entries.\n".format(vocab_table.Foreign.count()))
    return vocab_table


def initialize_Quiz():
    if not os.path.isfile('vocabulary.csv'):
        NoTable()

    else:
        vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
        # print("Initializing: Found existing table with {} entries.\n".format(vocab_table.Foreign.count()))
        return vocab_table

class NoTable:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('150x100')
        self.lbl1 = Label(self.root, text="No vocabulary found!\nAdd vocabulary first.")
        # self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')