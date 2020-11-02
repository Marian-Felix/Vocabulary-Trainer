from tkinter import *
#import add_vocab
from initialize import initialize
from add_vocab import AddVocab
from datetime import datetime



window = Tk()

# initialize vocabulary table (load/create)
vocab_table = initialize()

window.title("Vocabulary Trainer")
window.geometry('500x500')

lbl = Label(window, text="Hello")
lbl.config(font=('Arial', 44))
lbl.place(relx=0.5, rely=0.4, anchor="center")

lbl = Label(window, text="Current Mode ...")
lbl.place(relx=0.5, rely=0.3, anchor='center')

txt = Entry(window, width=18)
txt.place(relx=0.5, rely=0.8, anchor="center")

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

def clicked_add():
    lbl.configure(text= "Mode: \nAdd Vocabulary")

def clicked_enter():
    app = AddVocab()


def clicked_excel():
    dt_string = datetime.now().strftime("%d_%m_%Y %H-%M-%S")
    vocab_table.to_excel('Vocabulary {}.xlsx'.format(dt_string))


btn1 = Button(window, text="Add Vocabulary", command=clicked_add)
btn2 = Button(window, text="(Remove Vocabulary)", command=clicked)
btn3 = Button(window, text="(Practice!)", command=clicked)
btn4 = Button(window, text="Create Excel", command=clicked_excel)
btn5 = Button(window, text="    Enter    ", command=clicked_enter)

btn1.grid(column=0, row=0)
btn2.grid(column=1, row=0)
btn3.grid(column=2, row=0)
btn4.grid(column=3, row=0)

btn5.place(relx=0.5, rely=0.85, anchor='center')

window.mainloop()
