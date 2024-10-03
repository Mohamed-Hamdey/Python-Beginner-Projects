import pandas as pd

# Read the CSV file into a DataFrame
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Initialize an empty dictionary
nato_dict = {}
pheno_dict = {row.letter : row.code for (index ,row) in nato_df.iterrows()}

def generate_phen():
 word = input("Enter your word : ").upper()
 try:
   
    result = [pheno_dict[letter] for letter in word]
 except KeyError:
    print("sorry you can enter only alphabetic characters")
    generate_phen()
 else:    
    print(result)

generate_phen()