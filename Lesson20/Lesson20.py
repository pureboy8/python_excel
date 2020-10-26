# Section0 开场
print("-"*30 + "Begin Section 0 开场" + "-"*30)
print("这是Python的第二十次课程,主要讲数据可视化:")
print("1.Geo生成全国主要城市航班流动图")
print("-"*30 + "End Section 0 开场" + "-"*30)
print('\n')


from pyecharts import options as opts 
from pyecharts.charts import Geo
from pyecharts.globals import ThemeType,ChartType,SymbolType


data1=[("深圳",120),("哈尔滨",66),("杭州",77),("重庆","88"),("上海", 100), ("乌鲁木齐", 30),("北京", 30),("武汉",70)]
data2 = [("北京", "上海"), ("武汉", "深圳"),("重庆", "杭州"),("哈尔滨", "重庆"),("乌鲁木齐", "哈尔滨"),("深圳", "乌鲁木齐"),("武汉", "北京")]
c = (
	Geo(init_opts = opts.InitOpts(width = "1920px",height = "1080px",theme = ThemeType.DARK))
	.add_schema(maptype = "china")
	.add(
		"",
		data1,
		type_ = ChartType.EFFECT_SCATTER,
		color = "green"

		)
	.add(
		"",
		data2,
		type_ = ChartType.LINES,
		effect_opts = opts.EffectOpts(symbol = SymbolType.ARROW,symbol_size = 6,color = "blue"),
		linestyle_opts = opts.LineStyleOpts(curve = 0.2)
		)
	.set_series_opts(label_opts = opts.LabelOpts(is_show = False))
	.set_global_opts(title_opts = opts.TitleOpts(title = "全国主要城市航班路线和数量"))
	.render("geo_lines.html")

	)
