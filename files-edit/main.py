with open("file_to_read.txt", mode="r") as file:
    file.seek(0)  # Move the cursor back to the beginning
    content = file.read()

print(content)
