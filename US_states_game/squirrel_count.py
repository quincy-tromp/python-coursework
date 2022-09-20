import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

my_table = data.groupby("Primary Fur Color").size()
gray_squirrel_count = int(my_table["Gray"])
cinnamon_squirrel_count = int(my_table["Cinnamon"])
black_squirrel_count = int(my_table["Black"])
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")