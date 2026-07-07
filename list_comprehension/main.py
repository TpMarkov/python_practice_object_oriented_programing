numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
#
# print(new_list)


# Create copy of the numbers list and add 1 to each of its elements
new_list_of_numbers = [n + 1 for n in numbers]  # [2,3,4]
print(new_list_of_numbers)

# Create a list of elements from a string
letters_in_list = [letter for letter in 'Tsvetan']  # ["T","s","v","e","t","a","n"]
print(letters_in_list)

# Challenge to double nums in range 1 (incl) - 5 (excl)
doubled_nums = [num * 2 for num in [1, 2, 3, 4]]
print(doubled_nums)
