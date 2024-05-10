from file_define import TextFileRead, JsonFileRead
import data_define
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pyecharts.charts import Pie
from pyecharts import options as opts

text_file_reader = TextFileRead("D:/001.txt")
json_file_reader = JsonFileRead("D:/000.txt")
text_file_reader01 = TextFileRead("D:/002.txt")
file1: list[data_define.Record] = text_file_reader.read_data()
file2: list[data_define.Record] = text_file_reader01.read_data()
all_file = file1 + file2
dict1 = {}
dict2 = {}
dict3 = {}
for record in all_file:
    if record.data in dict1.keys():
        dict1[record.data] += record.money
    else:
        dict1[record.data] = record.money

for record in all_file:
    dict2[record.order_id] = record.province
for i in dict2.values():
    if i not in dict3.keys():
        dict3[i] = 1
    else:
        dict3[i] += 1
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))  # 美化颜色
bar.add_xaxis(list(dict1.keys()))
bar.add_yaxis("金额", list(dict1.values()), label_opts=LabelOpts(is_show=False))  # 输入y轴的值，并删除图形上的数字
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")  # 保存到本地文件

pie = Pie()
pie.add("", [list(z) for z in zip(dict3.keys(), dict3.values())])
pie.set_global_opts(title_opts=opts.TitleOpts(title="销售省份占比"))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
pie.render("销售省份占比饼状图.html")  # 绘制饼状图
