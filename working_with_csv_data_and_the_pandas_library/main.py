


# with open('weather_data.csv') as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         print(row)
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
import pandas
#check pandas documentation for functions
data = pandas.read_csv('weather_data.csv')
# print(data) # type Dataframe
# print(data["temp"]) # this does the same thig as rows 8-18 type Series

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# """count average without pandas"""
# # temp_sum = sum(temp_list)
# # list_len = len(temp_list)
# # average = temp_sum/list_len
# # print(average)
# """count average with pandas"""
# average = data["temp"].mean() # mean() has to use Series type
# print(average)
# maximum = data["temp"].max()
# print(maximum)

# """Get data in Row"""
print(data[data["day"] == "Monday"])
# """print maximum temperature row"""
max_temp = data["temp"].max()
print(data["temp"])
print(type(data["temp"]))
print(type(max_temp))
# print(data[data["temp"] == max_temp])
# monday = data[data["day"] == "Monday"]
# print(monday["condition"])
# monday_temp = data["temp"][0]
# monday_fahrenheit = (monday_temp * 1.8) + 32
# print(monday_fahrenheit)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(data["Primary Fur Color"])
# table = pandas.pivot_table(data, columns=["Primary Fur Color"], aggfunc="size")
# data_dict = table.to_dict()
# print(data_dict)
# colors = list(data_dict.keys())
# count = list(data_dict.values())
# # print(colors)
# # print(count)
# table_dict = {
#     "Primary Fur Color": list(data_dict.keys()),
#     "Count": list(data_dict.values())
# }
# print(table_dict)
# table_csv = pandas.DataFrame(table_dict)
# table_csv.to_csv("squirrel_colors.csv")

