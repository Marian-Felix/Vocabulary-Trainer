import pandas as pd

def user_input_to_df():
    english = input("Enter new English Term\n")
    german1 = input("Enter German meaning #1\n")
    german2 = input("Enter German meaning #2\n")
    german3 = input("Enter German meaning #3\n")
    new_vocab_df = pd.DataFrame({'English': [english], 'German1': [german1], 'German2': [german2], 'German3': [german3]})
    return new_vocab_df

