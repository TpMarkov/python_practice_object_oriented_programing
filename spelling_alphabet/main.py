import pandas


def spell_word(word):
    if len(word.split()) == 1:
        return [nato_words[letter] for letter in word.upper() if letter in nato_words]
    else:
        result = []
        words = word.split()
        for word in words:
            result.append([nato_words[letter] for letter in word.upper() if letter in nato_words])
        return result


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_words = {
    value.letter: value.code for
    index, value in data.iterrows()
}
print(nato_words)
word_to_replace = input("Please type in sentence to spell.")

print(spell_word(word_to_replace))
