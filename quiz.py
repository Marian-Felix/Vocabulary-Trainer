import pandas as pd
from tkinter import *


class Quiz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Quiz!")
        self.root.geometry('350x400')
        self.lbl1 = Label(self.root, text="\nQuiz!")
        self.lbl1.config(font=('Arial', 18))
        self.lbl1.place(relx=0.5, rely=0.1, anchor='center')

        self.lblInput_Foreign = Label(self.root, text="Foreign term:")
        self.lblInput_Foreign.place(relx=0.2, rely=0.3, anchor='center')
        self.input_Foreign = Entry(self.root, width=18)
        self.input_Foreign.place(relx=0.5, rely=0.3, anchor='center')

        self.lblInput_Transl1 = Label(self.root, text="Translation #1:")
        self.lblInput_Transl1.place(relx=0.2, rely=0.5, anchor='center')
        self.input_Transl1 = Entry(self.root, width=18)
        self.input_Transl1.place(relx=0.5, rely=0.5, anchor='center')

        self.lblInput_Transl2 = Label(self.root, text="Translation #2:")
        self.lblInput_Transl2.place(relx=0.2, rely=0.6, anchor='center')
        self.input_Transl2 = Entry(self.root, width=18)
        self.input_Transl2.place(relx=0.5, rely=0.6, anchor='center')

        self.lblInput_Transl3 = Label(self.root, text="Translation #3:")
        self.lblInput_Transl3.place(relx=0.2, rely=0.7, anchor='center')
        self.input_Transl3 = Entry(self.root, width=18)
        self.input_Transl3.place(relx=0.5, rely=0.7, anchor='center')

        self.btnEnter = Button(self.root, text="Submit answer", command=clicked_submit)
        self.btnEnter.config(height=3, width=18)
        self.btnEnter.place(relx=0.5, rely=0.85, anchor='center')

        self.root.mainloop()

    def clicked_submit():
        pass