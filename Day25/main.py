# with open("./day25/weather-data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)


# import csv
# with open("./day25/weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     tempatures = []
#     for row in data:
#         if row[1] != 'temp':
#             tempatures.append(int(row[1]))
#     print(tempatures)

import pandas as pd
# data = pd.read_csv("./Day25/weather-data.csv")
# print(data['temp'])
# print(type(data))
# print(type(data['temp']))

# data_frame = data.to_dict()
# print(data_frame)

# temp_list = data['temp'].to_list()
# # print(round( sum(temp_list) / len(temp_list), 2))
# print(data['temp'].max())
# print(data['temp'].min())
# print(data['temp'].mean())
# print(data['temp'].median())
# print(data['temp'].mode())

# # Get data in colomn
# print(data['condition'])
# print(data.condition)

# Get data in row
# print(data[data.day == 'Monday'])

# Get the maximum Temp. data in row
# print(data[data.temp == data.temp.max()])

# Get monday temp. 

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp*(9/5) + 35
# print(monday_temp_F)


# Create a dataframe from scratch
# data_dict = [{'a': 1, 'b': 2, 'c': 3},
#         {'a': 10, 'b': 20, 'c': 30}]
# data = pd.DataFrame(data_dict)
# data.to_csv("./day25/new_data.csv")

data = pd.read_csv("./Day25/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirells_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirells_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirells_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirells_count, red_squirells_count, black_squirells_count],
}

df = pd.DataFrame(data_dict)
csv_data = df.to_csv("./day25/Squirells_count.csv")