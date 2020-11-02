import pandas as pd
from tkinter import *


class AddVocab():
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root,
                              text="Label")
        self.buttonForget = Button(self.root,
                                      text='Click to hide Label',
                                      command=lambda: self.label.pack_forget())
        self.buttonRecover = Button(self.root,
                                       text='Click to show Label',
                                       command=lambda: self.label.pack())

        self.buttonForget.pack()
        self.buttonRecover.pack()
        self.label.pack(side="bottom")
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

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
def add_new_entry():
    new_entry = add_vocab.user_input_to_df()
    vocab_table = pd.concat([vocab_table, new_entry])
    print("New entry added: \n", new_entry, "\n")

    # add merged dataframe to .csv file
    vocab_table.reset_index(inplace=True, drop=True)
    vocab_table.to_csv('vocabulary.csv')
    print("Current Table: \n", vocab_table, "\n")