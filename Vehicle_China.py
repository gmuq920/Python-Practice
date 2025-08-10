from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
# from pyecharts.globals import ThemeType
import json

#open file
f = open("Vehicle_Data.txt","r",encoding="UTF-8")

#read file and  save to py
data_read = f.read()

#close file
f.close()

#use json loads
data_read = json.loads(data_read)

#set up a new dictionary
dict_new = {}

#use for loop to reset the dict
for month in data_read:
    month_value = month["month"]
    #print(month_value)
    data_list = []
    data_dict = month["sales"]
    keys = data_dict.keys()
    for key in keys:
        data_list.append([key,data_dict[key]])
    dict_new[month_value] = data_list

#set up timeline
timeline = Timeline()

#sort by year
sorted_year_list = sorted(dict_new.keys())
for year in sorted_year_list:
    year_data = dict_new[year]
    x_data = []
    y_data = []
    for brand in year_data:
        x_data.append(brand[0])
        y_data.append(brand[1]/1000)

    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("Sales(Thousand)",y_data,label_opts=LabelOpts(position="right"))

    #reverse the axis
    bar.reversal_axis()

    timeline.add(bar,str(year))

#set timeline play interval = 500 autoplay=true
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("Chinese car market over the past 60 months.html")










