import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231203.csv")
fur = data["Primary Fur Color"].to_list()
c_cin = 0
c_b = 0
c_g = 0
for color in fur:
    if color == "Gray":
        c_g += 1
    elif color == "Cinnamon":
        c_cin += 1
    elif color == "Black":
        c_b += 1

data_dict = {"colors": ["Gray", "Cinnamon", "Black"],
             "counts": [c_g, c_cin, c_b]}
data_frame = pd.DataFrame(data_dict)
data_frame.to_csv("colors_count.csv")


