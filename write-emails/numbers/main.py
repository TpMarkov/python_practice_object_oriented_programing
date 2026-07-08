with open("file1.txt", "r+") as file_1:
    nums_1 = [int(n) for n in file_1.read().split()]

with open("file2.txt", "r+") as file_2:
    nums_2 = [int(n) for n in file_2.read().split()]

result = [int(n) for n in nums_1 if n in nums_2 and n != "\n"]

print(result)
