import pandas as pd
from tkinter import *
# from main import vocab_table
from initialize import initialize

class AddVocab:
    def __init__(self):
        self.vocab_table = initialize()

        self.root = Tk()
        self.root.title("Add Vocabulary")
        self.root.geometry('350x400')
        self.lbl1 = Label(self.root, text="\nAdd new vocabulary!")
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

        self.btnEnter = Button(self.root, text="Add Vocabulary", command=clicked_add)
        self.btnEnter.config(height=3, width=18)
        self.btnEnter.place(relx=0.5, rely=0.85, anchor='center')
        self.root.mainloop()

    def user_input_to_df(self):
        new_vocab_df = pd.DataFrame(
            {'English': [self.input_Foreign], 'German1': [self.input_Transl1], 'German2': [self.input_Transl2],
             'German3': [self.input_Transl3]})

        new_vocab_table = pd.concat([self.vocab_table, new_vocab_df])
        new_vocab_table.reset_index(inplace=True, drop=True)
        new_vocab_table.to_csv('vocabulary.csv')
        self.vocab_table = new_vocab_table

    def clicked_add():
        pass









def user_input_to_df():
    english = input("Enter new English Term\n")
    german1 = input("Enter German meaning #1\n")
    german2 = input("Enter German meaning #2\n")
    german3 = input("Enter German meaning #3\n")
    new_vocab_df = pd.DataFrame({'English': [english], 'German1': [german1], 'German2': [german2], 'German3': [german3]})
    return new_vocab_df

def user_input_to_df():
    english = input("Enter new English Term\n")
    german1 = input("Enter German meaning #1\n")
    german2 = input("Enter German meaning #2\n")
    german3 = input("Enter German meaning #3\n")
    new_vocab_df = pd.DataFrame({'English': [english], 'German1': [german1], 'German2': [german2], 'German3': [german3]})
    return new_vocab_df


# add new entries

# create single row dataframe from user input, add to existing dataframe
"""def add_new_entry():
    new_entry = add_vocab.user_input_to_df()
    vocab_table = pd.concat([vocab_table, new_entry])
    print("New entry added: \n", new_entry, "\n")

    # add merged dataframe to .csv file
    vocab_table.reset_index(inplace=True, drop=True)
    vocab_table.to_csv('vocabulary.csv')
    print("Current Table: \n", vocab_table, "\n")"""

