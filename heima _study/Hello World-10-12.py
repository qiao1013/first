#           10章

# import json
#把列表转换成json
""" data=[{"name":"张三","age":"18"},{"name":"李四","age":"19"},{"name":"王五","age":"20"}] 
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

data1 = {"name":"周杰伦","addr":"台北"}
json_str2 = json.dumps(data1,ensure_ascii=False)
print(json_str2) """
# 把json转换为python的数据格式
""" data = '[{"name": "张三", "age": "18"}, {"name": "李四", "age": "19"}, {"name": "王五", "age": "20"}]'#       因为是字符串所以加''
l = json.loads(data)
print(type(l))
print(l)

data1 = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(data1)
print(type(l))
print(l) """

#    ------------------------------------第10章-------------------------------#
#             pyecharts模块基础使用 全局配置
""" from pyecharts.charts import Line                                       # 从pyecharts包中的charts模块引入 Line函数  其实就是画了一个x轴一个Y轴
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line = Line()                                                           # line =的作用 将创建好的折线图对象赋值给变量 line    这样后续就可以通过 line这个变量来操作图表
line.add_xaxis(['中国','美国','日本'])                                   #x轴
line.add_yaxis("GDP",[50,20,10])                                        #y轴
line.set_global_opts(
    title_opts = TitleOpts("全国GDP",pos_top="center",pos_left="50%"),
    legend_opts= LegendOpts(is_show =True),
    toolbox_opts= ToolboxOpts(is_show = True),
    visualmap_opts= VisualMapOpts(is_show = True)
)

line.render()                                #进行图像显示 生成浏览器可以打开的文件 """

# 2020年疫情折线图——————————————————————————————————————————————————设计
from pyecharts.charts import Line       #导入图表
from pyecharts.options import TitleOpts,LabelOpts                   #导入的两个类
import json
#   处理数据
us_file = open("D:/美国.txt",'r',encoding='UTF-8')
us_file_data = us_file.read()

jp_file = open("D:/日本.txt",'r',encoding='UTF-8')
jp_file_data = jp_file.read()

in_file = open("D:/印度.txt",'r',encoding='UTF-8')
in_file_data = in_file.read()
# 去掉json不合规的开头
us_file_data = us_file_data.replace("jsonp_1629344292311_69436(",'')
jp_file_data = jp_file_data.replace("jsonp_1629350871167_29498(",'')
in_file_data = in_file_data.replace("jsonp_1629350745930_63180(",'')

# 去掉json不合规的结尾
us_file_data = us_file_data[:-2]
jp_file_data = jp_file_data[:-2]
in_file_data = in_file_data[:-2]

#json转字典
us_dict = json.loads(us_file_data)
jp_dict = json.loads(jp_file_data)
in_dict = json.loads(in_file_data)

#取到trend key
us_trend_dict = us_dict['data'][0]['trend']
jp_trend_dict = jp_dict['data'][0]['trend']
in_trend_dict = in_dict['data'][0]['trend']

#取到日期，换做为x轴数据 
us_x = us_trend_dict['updateDate'][:314]#x轴公用
#取到确诊人数， 换做为y轴数据
us_y = us_trend_dict['list'][0]['data'][:314]
jp_y = jp_trend_dict['list'][0]['data'][:314]
in_y = in_trend_dict['list'][0]['data'][:314]
#x轴y轴都有了，可以创建图表了，将创建好的Line图标对象赋值给line
# 构建Line折线图表对象
line = Line()
#添加x轴数据到折线图中
line.add_xaxis(us_x)
#添加y轴数据
line.add_yaxis("美国确诊人数",us_y,label_opts=LabelOpts(is_show = False))
line.add_yaxis("日本确诊人数",jp_y,label_opts=LabelOpts(is_show = False))
line.add_yaxis("印度确诊人数",in_y,label_opts=LabelOpts(is_show = False))
#设置全局选项
line.set_global_opts(
    #标题设置
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比图',pos_left='center',pos_top='1%')
    #
)

#调用render生成图表
line.render()
#关闭
us_file.close()
jp_file.close()
in_file.close()

#如果最后要关闭文件，那么打开文件的变量只能用一次，后面更新变量

