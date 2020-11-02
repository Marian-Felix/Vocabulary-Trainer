import os.path
import pandas as pd
from tkinter import *


class Quiz:
    def __init__(self):
        # read existing table or create new one
        self.vocab_table = self.initialize_table()
        # self.quiz_range = self.vocab_table.Foreign.count()
        # print(self.vocab_table.iloc[0][0])

        self.root = Tk()
        self.root.title("Vocab!")
        self.root.geometry('350x400')
        self.lbl1 = Label(self.root, text="\nQuiz!")
        self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.1, anchor='center')

        self.lblInput_Foreign = Label(self.root, text="Foreign term:")
        self.lblInput_Foreign.place(relx=0.3, rely=0.3, anchor='center')
        self.input_Foreign = Entry(self.root, width=18)
        self.input_Foreign.place(relx=0.6, rely=0.3, anchor='center')

        self.lblTransl1 = Label(self.root, text="Meaning #1:")
        self.lblTransl1.place(relx=0.3, rely=0.5, anchor='center')
        self.Transl1 = Label(self.root, text="Test Begriff")
        self.Transl1.place(relx=0.6, rely=0.5, anchor='center')

        self.lblTransl2 = Label(self.root, text="Meaning #2:")
        self.lblTransl2.place(relx=0.3, rely=0.6, anchor='center')
        self.Transl2 = Label(self.root, text="Test Begriff")
        self.Transl2.place(relx=0.6, rely=0.6, anchor='center')

        self.lblTransl3 = Label(self.root, text="Meaning #3:")
        self.lblTransl3.place(relx=0.3, rely=0.7, anchor='center')
        self.Transl3 = Label(self.root, text="Test Begriff")
        self.Transl3.place(relx=0.6, rely=0.7, anchor='center')

        self.btnDelete = Button(self.root, text="Delete\nEntry", command=self.clicked_delete)
        self.btnDelete.config(height=2, width=5)
        self.btnDelete.place(relx=0.93, rely=0.05, anchor='center')

        self.btnSubmit = Button(self.root, text="Submit answer", command=self.clicked_submit)
        self.btnSubmit.config(height=3, width=18)
        self.btnSubmit.place(relx=0.5, rely=0.85, anchor='center')


        self.root.mainloop()


    def initialize_table(self):
        if not os.path.isfile('vocabulary.csv'):
            NoTable()

        else:
            vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
            return vocab_table

    def clicked_submit(self):
        pass

    def clicked_delete(self):
        pass


class NoTable:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('150x100')
        self.lbl1 = Label(self.root, text="No entries found.\n\nAdd vocabulary first!")
        # self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')