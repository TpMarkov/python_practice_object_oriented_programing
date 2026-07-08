import random
import pandas

STARTING_LETTER = "b"
numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
#
# print(new_list)


# Create copy of the numbers list and add 1 to each of its elements
new_list_of_numbers = [n + 1 for n in numbers]  # [2,3,4]
# print(new_list_of_numbers)

# Create a list of elements from a string
letters_in_list = [letter for letter in 'Tsvetan']  # ["T","s","v","e","t","a","n"]
# print(letters_in_list)

# Challenge to double nums in range 1 (incl) - 5 (excl)
doubled_nums = [num * 2 for num in [1, 2, 3, 4]]
# Alternatively
doubled_numbers = [num * 2 for num in range(1, 5)
                   ]

# if condition in list comprehension
names = ["Alex", "Beth", "Caroline", "Tsvetan", "Dave", "Bobby", "Adrenalinna", "anita"]

short_names = [n for n in names if len(n) < 5]

names_starting_with_a = [n for n in names if
                         n.startswith(STARTING_LETTER.upper()) or n.startswith(STARTING_LETTER.lower())]

# print(doubled_numbers)
# print(doubled_nums)
# print(short_names)
# print(names_starting_with_a)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(f"SQUARED NUMBERS:\n{squared_numbers}")

print("--------------------------------------")

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
result_of_converted_even_numbers = [int(n) for n in list_of_strings if int(n) % 2 == 0]
print(f"FILTERED EVEN NUMBERS:\n{result_of_converted_even_numbers}")

print("--------------------------------------")

# We can also use comprehension to create dictionaries

students_names = ["ALex", "Beth", "Caroline", "Tsvetan", "Dave", "Boby", "Adrenalita", "anita"]
print(f"Creating dictionary using the 'comprehension' technique:")
PASSING_SCORE = 70

students_scores = {name: random.randint(1, 100)
                   for name in students_names}

passed_students = {
    student: score
    for student, score in students_scores.items()  # We are taking the key and the value in a list pair [key, value]
    if score >= PASSING_SCORE
}

print(students_scores)
print("--------------------------------------")

#
print(f"HERE ARE THE STUDENTS THAT PASSES THE EXAM WITH MORE THEN {PASSING_SCORE} POINTS: \n{passed_students}")
print("--------------------------------------")

sentence = "Calculate the number of letters for each of the words in this sentence"

words_data = {
    word: len(word) for word in sentence.split()
}

print(f"Printing the length of words in a sentence: \n"
      f"{words_data}"
      )
print("--------------------------------------")

# Loop through a DataFrame
student_data = {
    "Name": ["Adrian", "Anna", "Anabel"],
    "Score": [30, 50, 60]
}

student_data_frame = pandas.DataFrame(student_data)

# Iterate trough each of the rows in a dataFrame
for (index, row) in student_data_frame.iterrows():
    print(row)
