import os.path
import pandas as pd
from tkinter import *
import random


class Quiz:
    def __init__(self):
        # set up GUI
        self.root = Tk()
        self.root.title("Vocab!")
        self.root.geometry('350x400')

        self.lbl1 = Label(self.root, text="\nQuiz!")
        self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.1, anchor='center')

        self.lblEvaluation = Label(self.root)
        self.lblEvaluation.config(font=('Arial', 28, 'bold'))
        self.lblEvaluation.place(relx=0.5, rely=0.55, anchor='center')

        self.lblRightAnswer = Label(self.root)
        self.lblRightAnswer.config(font=('Arial', 10, 'bold'))

        self.lblInput_Foreign = Label(self.root, text="Foreign term:")
        self.lblInput_Foreign.place(relx=0.3, rely=0.3, anchor='center')
        self.input_Foreign = Entry(self.root, width=18)
        self.input_Foreign.place(relx=0.6, rely=0.3, anchor='center')

        self.place_meanings()

        self.btnDelete = Button(self.root, text="Delete\nEntry", command=self.clicked_delete)
        self.btnDelete.config(height=2, width=5)
        self.btnDelete.place(relx=0.93, rely=0.05, anchor='center')

        self.btnSubmit = Button(self.root, text="Submit answer", command=self.clicked_submit)
        self.btnSubmit.config(height=3, width=18)
        self.btnSubmit.place(relx=0.5, rely=0.85, anchor='center')

        # read existing table or create new one, create index list for quiz term retrieval
        self.vocab_table = self.initialize_table()

        self.quiz_range = list(range(self.vocab_table.Foreign.count()))
        random.shuffle(self.quiz_range)

        self.get_quiz_term()

        self.root.mainloop()


    def initialize_table(self):
        if not os.path.isfile('vocabulary.csv'):
            NoTable()
            self.root.destroy()

        else:
            vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
            return vocab_table


    def get_quiz_term(self):
        try:
            self.quiz_index = self.quiz_range.pop()
        except IndexError:
            QuizFinished()
            self.root.destroy()
        print(self.quiz_index)
        print(self.quiz_range)
        self.quiz_foreign = self.vocab_table.iloc[self.quiz_index][0]
        self.quiz_meaning1 = self.vocab_table.iloc[self.quiz_index][1]
        self.quiz_meaning2 = self.vocab_table.iloc[self.quiz_index][2]
        self.quiz_meaning3 = self.vocab_table.iloc[self.quiz_index][3]
        self.Transl1.configure(text=self.quiz_meaning1)
        self.Transl2.configure(text=self.quiz_meaning2)
        self.Transl3.configure(text=self.quiz_meaning3)


    def hide_meanings(self):
        self.lblTransl1.place_forget()
        self.lblTransl2.place_forget()
        self.lblTransl3.place_forget()
        self.Transl1.place_forget()
        self.Transl2.place_forget()
        self.Transl3.place_forget()

    def place_meanings(self):
        self.lblTransl1 = Label(self.root, text="Meaning #1:")
        self.lblTransl1.place(relx=0.3, rely=0.5, anchor='center')
        self.Transl1 = Label(self.root)
        self.Transl1.config(font=('Arial', 10, 'bold'))
        self.Transl1.place(relx=0.6, rely=0.5, anchor='center')

        self.lblTransl2 = Label(self.root, text="Meaning #2:")
        self.lblTransl2.place(relx=0.3, rely=0.6, anchor='center')
        self.Transl2 = Label(self.root)
        self.Transl2.config(font=('Arial', 10, 'bold'))
        self.Transl2.place(relx=0.6, rely=0.6, anchor='center')

        self.lblTransl3 = Label(self.root, text="Meaning #3:")
        self.lblTransl3.place(relx=0.3, rely=0.7, anchor='center')
        self.Transl3 = Label(self.root)
        self.Transl3.config(font=('Arial', 10, 'bold'))
        self.Transl3.place(relx=0.6, rely=0.7, anchor='center')


    def clicked_submit(self):
        print(self.input_Foreign.get() == self.quiz_foreign)
        self.hide_meanings()
        self.lblEvaluation.place(relx=0.5, rely=0.55, anchor='center')

        if self.input_Foreign.get() == self.quiz_foreign:
            self.lblEvaluation.config(fg='green', text='Correct!')

        else:
            self.lblEvaluation.config(fg='orange', text='Incorrect')
            self.lblRightAnswer.config(text='Correct answer: {}'.format(self.quiz_foreign))
            self.lblRightAnswer.place(relx=0.5, rely=0.65, anchor='center')

        self.btnSubmit.config(text='OK', command=self.clicked_confirm)


    def clicked_confirm(self):
        self.lblEvaluation.place_forget()
        self.lblRightAnswer.place_forget()
        self.place_meanings()
        self.get_quiz_term()
        print(self.quiz_foreign)
        self.btnSubmit.config(text='Submit answer', command=self.clicked_submit)


    def clicked_delete(self):
        if self.vocab_table.Foreign.count() > 0:
            self.vocab_table.drop(self.quiz_index, inplace=True)
            self.vocab_table.reset_index(inplace=True, drop=True)
            self.quiz_range = list(range(self.vocab_table.Foreign.count()))
            random.shuffle(self.quiz_range)
            print(self.vocab_table)
            print(self.quiz_index)
            self.vocab_table.to_csv('vocabulary.csv')
            self.clicked_submit()
            self.clicked_confirm()
            DeleteSuccesful()
            print("Delete succesful!")
        else:
            NoTable()

# confirmation pop-up windows
class NoTable:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('150x100')
        self.lbl1 = Label(self.root, text="No entries found.\n\nAdd vocabulary first!")
        # self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')

class QuizFinished:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('150x100')
        self.lbl1 = Label(self.root, text="No more entries.\nNice work!")
        # self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')

class Congrats:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('150x100')
        self.lbl1 = Label(self.root, text="Correct!")
        # self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')

class DeleteSuccesful:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('150x100')
        self.lbl1 = Label(self.root, text="Entry deleted!")
        # self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.5, anchor='center')