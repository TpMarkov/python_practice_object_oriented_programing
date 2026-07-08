import pandas


def spell_word(word):
    return [nato_words[letter] for letter in word.upper()]

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_words = {
    value.letter: value.code for
    index, value in data.iterrows()
}
print(nato_words)

word_to_replace = input("Please type in sentence to spell.")

print(spell_word(word_to_replace))
