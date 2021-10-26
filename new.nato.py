import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")

new_dic = {}
for (index, row) in file.iterrows():
    lett = row.letter
    new_dic[lett] = row.code


def alphabet_generator():
    user_input = input("give me a word: ").upper()
    try:
        result = [new_dic[item] for item in user_input]
    except KeyError:
        print("Sorry, please letters are only alphabet")
        alphabet_generator()
    else:
        print(result)

alphabet_generator()