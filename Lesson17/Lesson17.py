# Section0 开场
print("-"*30 + "Begin Section 0 开场" + "-"*30)
print("这是Python的第十七次课程,主要讲数据可视化:")
print("1.水球图\n2.平行坐标系\n3.极坐标系\n4.雷达图")
print("-"*30 + "End Section 0 开场" + "-"*30)
print('\n')

from pyecharts import options as opts
# Section1 水球图

from pyecharts.charts import Grid,Liquid
from pyecharts.commons.utils import JsCode

# [0.4,0.7]前面是现实的label的值，后面是水波占整个的比例
l1 = (
	Liquid()
	.add("lq",[0.4,0.7],is_outline_show = False,shape = "diamond")
	.set_global_opts(title_opts = opts.TitleOpts(title = "Liquid-Shape-Diamond"))
	.render("liquid_shape_diamond.html")
	)

# 多个水球图显示
l1 = (
	Liquid()
	.add("lq",[0.6,0.7],center = ["60%","50%"])
	.set_global_opts(title_opts = opts.TitleOpts(title = "多个Liquid显示"))
	)

# JsCode里面的%只能是单引号，双引号不会报错，但是结果也不会显示
# Math.floor() 向下取整
l2 = Liquid().add(
			"lq",
			[0.3254],
			center = ["25%","50%"],
			label_opts = opts.LabelOpts(
				font_size = 50,
				formatter = JsCode(
					"""function (param){
						return (Math.floor(param.value * 10000)/100) + '%';  

					}"""
					),
				position = "inside",
				),
	)

	
	

grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
grid.render("multiple_liquid.html")


# Section2 平行坐标系
from pyecharts.charts import Parallel

data = [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"],
]

c = (
	Parallel()
	.add_schema(
		[
			opts.ParallelAxisOpts(dim = 0,name = "data"),
			opts.ParallelAxisOpts(dim = 1,name = "AQI"),
			opts.ParallelAxisOpts(dim = 2,name = "PM2.5"),
			opts.ParallelAxisOpts(dim = 3,name = "PM10"),
			opts.ParallelAxisOpts(dim = 4,name = "CO"),
			opts.ParallelAxisOpts(dim = 5,name = "NO2"),
			opts.ParallelAxisOpts(dim = 6,name = "CO2"),
			opts.ParallelAxisOpts(
				dim = 7,
				name ="等级",
				type_ = "category",
				data = ["优","良","轻度污染","中度污染","重度污染","严重污染"],
				),

		]

		)
	.add(
		"parallel",
		data,
		)
	.set_global_opts(title_opts = opts.TitleOpts(title = "Parallel-Category"))
	.render("parallel_category.html")


	)

# Section3 极坐标系
# 爱心图
import math
from pyecharts.charts import Polar
data = []
for i in range(101):
	theta = i / 100 * 360
	r = 5 * (1 + math.sin(theta / 180 * math.pi))
	data.append([r,theta])
hour = [i for i in range(1,15)]
c = (
	Polar()
	.add_schema(
		angleaxis_opts = opts.AngleAxisOpts(
			start_angle = 0
			)
		)
	.add("love",data,label_opts = opts.LabelOpts(is_show = False))
	.set_global_opts(title_opts = opts.TitleOpts(title = "Polar-Love"))
	.render("polar_love.html")
	)


# 水溅的效果
import random
data = [(i,random.randint(1,100)) for i in range(10)]
c = (
	Polar()
	.add(
		"",
		data,
		type_ = "effectScatter",
		effect_opts = opts.EffectOpts(scale = 10,period = 5),
		label_opts = opts.LabelOpts(is_show = False),
		)
	.set_global_opts(title_opts = opts.TitleOpts(title = "Polar-EffectScatter"))
	.render("polar_effectscatter.html")


	)


# Section4 雷达图
from pyecharts.charts import Radar
value_bj = [
    [55, 9, 56, 0.46, 18, 6, 1],
    [25, 11, 21, 0.65, 34, 9, 2],
    [56, 7, 63, 0.3, 14, 5, 3],
    [33, 7, 29, 0.33, 16, 6, 4],
    [42, 24, 44, 0.76, 40, 16, 5],
    [82, 58, 90, 1.77, 68, 33, 6],
    [74, 49, 77, 1.46, 48, 27, 7],
    [78, 55, 80, 1.29, 59, 29, 8],
    [267, 216, 280, 4.8, 108, 64, 9],
    [185, 127, 216, 2.52, 61, 27, 10],
    [39, 19, 38, 0.57, 31, 15, 11],
    [41, 11, 40, 0.43, 21, 7, 12],
]
value_sh = [
    [91, 45, 125, 0.82, 34, 23, 1],
    [65, 27, 78, 0.86, 45, 29, 2],
    [83, 60, 84, 1.09, 73, 27, 3],
    [109, 81, 121, 1.28, 68, 51, 4],
    [106, 77, 114, 1.07, 55, 51, 5],
    [109, 81, 121, 1.28, 68, 51, 6],
    [106, 77, 114, 1.07, 55, 51, 7],
    [89, 65, 78, 0.86, 51, 26, 8],
    [53, 33, 47, 0.64, 50, 17, 9],
    [80, 55, 80, 1.01, 75, 24, 10],
    [117, 81, 124, 1.03, 45, 24, 11],
    [99, 71, 142, 1.1, 62, 42, 12],
]

c_schema = [
	{"name":"AQI","max":300,"min":5},
	{"name":"PM2.5","max":250,"min":20},
	{"name":"PM10","max":300,"min":5},
	{"name":"CO","max":5},
	{"name":"NO2","max":200},
	{"name":"SO2","max":100},
]

c = (
	Radar()
	.add_schema(schema = c_schema,shape = "circle")
	.add("北京",value_bj,color = "#f9713c")
	.add("上海",value_sh,color = "#b3e4a1")
	.set_series_opts(label_opts = opts.LabelOpts(is_show = False))
	.set_global_opts(title_opts = opts.TitleOpts(title = "Radar-空气质量"))
	.render("radar_air_quality.html")


	)

