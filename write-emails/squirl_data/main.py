import pandas

# Read the csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Access the required data from the file
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

# Create the structure for the new CSV file and assign the values
new_data_format = {
    "Squirrel Colors"
    "Squirrels Count": [grey_squirrels, red_squirrels, black_squirrels]\
}

# Create the actual DataFrame from the created structure for the data
new_data_format = pandas.DataFrame(new_data_format)
# Convert the file to csv format
new_data_format.to_csv("new_squirrels_data.csv")
