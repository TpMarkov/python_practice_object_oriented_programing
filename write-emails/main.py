import csv
from pydoc_data import topics

import pandas

names = ["Irina", "Momchil", "Plamen", "Julia", "Katrin"]
print("Here are all the invitations sent!\n")

for name in names:
    # Naming the file
    filename = f"./letters/Invitation-{name.capitalize()}.txt"

    with open(filename, "w+") as letter:
        # Write the individual invitations and replace the name placeholder
        letter.write(f"Dear {name},\n"
                     "You are invited to my birthday this Saturday.\n"
                     "Hope you can make it!\n"
                     "Tsvetan")

    with open(filename, "r") as letter:
        print(letter.read())

        print("-----------------------------------------------------")

# Reading data from a CSV file - Coma-separated-values
# with open("weather_data/weather_data.csv") as weather:
#     data = weather.readlines()
#     for row in data:
#         print(row)


# Using built-in library to read CSV-files
with open("weather_data/weather_data.csv", newline="") as weather:
    reader = csv.reader(weather)
    next(reader)

    with open("weather_data/temperatures.txt", "w") as temp_file:
        for row in reader:
            temperature = row[1]
            # print(temperature)
            temp_file.write(temperature + "\n")

# Use pandas to read CSV - best choice
data = pandas.read_csv("weather_data/weather_data.csv")

# access particular row in a csv table file
print(f"{data["temp"]}\n")
to_dict = data.to_dict("records")
temperatures_to_list = data["temp"]

# method of calculating average value
print(temperatures_to_list.mean())
max_temp = (data["temp"].max())  # or use alternatively temperatures_to_list.max()

# Access and print data that meets a criteria
print(f"{data[data.temp == max_temp]}\n")  # meets the condition for max temp
print(f"{data[data.temp == 12].to_dict("records")}\n")  # meets the condition for all days that's been 12 degrees

# Create DataFrame table from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [2, 5, 6],
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
