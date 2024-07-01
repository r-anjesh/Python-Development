# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("./Day26/nato_phonetic_alphabet.csv")

fullform = {row.letter:row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word : ").upper()
phonetic_code = [fullform[letter] for letter in user_word]
print(phonetic_code)