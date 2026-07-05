names = ["Irina", "Momchil", "Plamen", "Julia", "Katrin"]

for name in names:
    with open(f"./letters/{name}.txt", "w+") as letter:
        letter.write(f"Dear {name},\n"
                     "You are invited to my birthday this Saturday.\n"
                     "Hope you can make it!\n"
                     "Tsvetan")
