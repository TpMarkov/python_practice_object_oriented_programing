with open("C:/Users/marko/OneDrive/Desktop/file_to_read.txt", "r+") as file:
    # file.write("\nAdd some new line to this file.")
    # file.write("\nAdd another line before seeking and then reading.")
    file.seek(
        0)  # Returns the cursor to the beginning of the file so that everything from top to bottom can print out from line 9

    content = file.read()

print(content)
