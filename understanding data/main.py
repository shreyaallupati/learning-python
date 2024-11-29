# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)


#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

#data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(temp_list)

#print(data["temp"].max())
#print(data.condition)

#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)

#create data frame from scratch
#data_dict = {
#    "students": ["amy", "james", "angela"],
#    "scores": [76, 56, 65]
#}
#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data.csv")





import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_fur_color = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "count": [f"{gray_squirrels_count}", f"{cinnamon_squirrels_count}",f"{black_squirrels_count}"]
}

data = pandas.DataFrame(data_fur_color)

print(data_fur_color)
data.to_csv("squirrel data")