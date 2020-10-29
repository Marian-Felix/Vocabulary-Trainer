import pandas as pd
import os.path
import add_vocab

# read existing .csv table or create new one
if not os.path.isfile('vocabulary.csv'):
    vocab_table = pd.DataFrame(columns=['English', 'German1', 'German2', 'German3'])
    vocab_table.to_csv('vocabulary.csv')
    print("Initializing: Could not find existing table. Created new table.\n")

else:
    vocab_table = pd.read_csv('vocabulary.csv', index_col=[0])
    print("Initializing: Found existing table with {} entries.\n".format(vocab_table.English.count()))


# add new entries
while vocab_table.English.count() < 2000:

    # create single row dataframe from user input, add to existing dataframe
    new_entry = add_vocab.user_input_to_df()
    vocab_table = pd.concat([vocab_table, new_entry])
    print("New entry added: \n", new_entry, "\n")

    # add merged dataframe to .csv file
    vocab_table.reset_index(inplace=True, drop=True)
    vocab_table.to_csv('vocabulary.csv')
    print("Current Table: \n", vocab_table, "\n")
