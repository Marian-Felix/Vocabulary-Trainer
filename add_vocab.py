import os.path
import pandas as pd
from tkinter import *


class AddVocab:
    def __init__(self):
        # read existing table or create new one
        self.vocab_table = self.initialize_table()

        # set up GUI
        self.root = Tk()
        self.root.eval('tk::PlaceWindow . center') # centers window
        self.root.title("Vocab!")
        self.root.geometry('350x400')
        self.lbl1 = Label(self.root, text="\nAdd new vocabulary!")
        self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.1, anchor='center')

        self.lblInput_Foreign = Label(self.root, text="Foreign term:")
        self.lblInput_Foreign.place(relx=0.3, rely=0.3, anchor='center')
        self.input_Foreign = Entry(self.root, width=18)
        self.input_Foreign.place(relx=0.6, rely=0.3, anchor='center')

        self.lblInput_Transl1 = Label(self.root, text="Meaning #1:")
        self.lblInput_Transl1.place(relx=0.3, rely=0.5, anchor='center')
        self.input_Transl1 = Entry(self.root, width=18)
        self.input_Transl1.place(relx=0.6, rely=0.5, anchor='center')

        self.lblInput_Transl2 = Label(self.root, text="Meaning #2:")
        self.lblInput_Transl2.place(relx=0.3, rely=0.6, anchor='center')
        self.input_Transl2 = Entry(self.root, width=18)
        self.input_Transl2.place(relx=0.6, rely=0.6, anchor='center')

        self.lblInput_Transl3 = Label(self.root, text="Meaning #3:")
        self.lblInput_Transl3.place(relx=0.3, rely=0.7, anchor='center')
        self.input_Transl3 = Entry(self.root, width=18)
        self.input_Transl3.place(relx=0.6, rely=0.7, anchor='center')

        self.btnAddVocab = Button(self.root, text="Add Vocabulary", command=self.clicked_add)
        self.btnAddVocab.config(height=3, width=18)
        self.btnAddVocab.place(relx=0.5, rely=0.85, anchor='center')

        self.root.mainloop()

    # read inputs (max. string length = 25) and add to table, then closes window
    def clicked_add(self):
        new_vocab_df = pd.DataFrame(
            {'Foreign': [self.input_Foreign.get()[:25]], 'Meaning1': [self.input_Transl1.get()[:25]], 'Meaning2': [self.input_Transl2.get()[:25]],
             'Meaning3': [self.input_Transl3.get()[:25]]})

        new_vocab_table = pd.concat([self.vocab_table, new_vocab_df])
        new_vocab_table.reset_index(inplace=True, drop=True)
        new_vocab_table.to_csv('vocabulary.csv')
        self.root.destroy()

    def initialize_table(self):
        if not os.path.isfile('vocabulary.csv'):
            vocab_table = pd.DataFrame(columns=['Foreign', 'Meaning1', 'Meaning2', 'Meaning3'])
            vocab_table.to_csv('vocabulary.csv')
            print("Initializing: Could not find existing table. Created new table.\n")

        else:
            vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
            print("Initializing: Found existing table with {} entries.\n".format(vocab_table.Foreign.count()))
        return vocab_table





