# Section0 开场
print("-"*30 + "Begin Section 0 开场" + "-"*30)
print("这是Python的第十八次课程,主要讲数据可视化:")
print("1.桑基图\n2.旭日图\n3.主题河流图\n4.词云图")
print("-"*30 + "End Section 0 开场" + "-"*30)
print('\n')


from pyecharts import options as opts

# Section1 桑基图
import json
from pyecharts.charts import Sankey

with open("product.json","r",encoding = "utf-8") as f:
	j = json.load(f)

c = (
	Sankey()
	.add(
		"sankey",
		nodes = j["nodes"],
		links = j["links"],
		pos_top = "10%",
		focus_node_adjacency = True,
		levels = [
			opts.SankeyLevelsOpts(
				depth = 0,
				itemstyle_opts = opts.ItemStyleOpts(color = "#fbb4ae"),
				linestyle_opts = opts.LineStyleOpts(color = "source",opacity = 0.6),
				),
			opts.SankeyLevelsOpts(
				depth = 1,
				itemstyle_opts = opts.ItemStyleOpts(color = "#b3cde3"),
				linestyle_opts = opts.LineStyleOpts(color = "source",opacity = 0.6),
				),
			opts.SankeyLevelsOpts(
				depth = 2,
				itemstyle_opts = opts.ItemStyleOpts(color = "#ccebc5"),
				linestyle_opts = opts.LineStyleOpts(color = "source",opacity = 0.6),
				),
			opts.SankeyLevelsOpts(
				depth = 3,
				itemstyle_opts = opts.ItemStyleOpts(color = "#decbe4"),
				linestyle_opts = opts.LineStyleOpts(color = "source",opacity = 0.6),
				)

		],
		linestyle_opt = opts.LineStyleOpts(curve = 0.5),
		)
	.set_global_opts(
		title_opts = opts.TitleOpts(title = "Sankey-Level Settings"),
		tooltip_opts = opts.TooltipOpts(trigger = "item",trigger_on = "mousemove"),
		)
	.render("sankey_with_level_setting.html")

	)


# Section2 旭日图
from pyecharts.charts import Sunburst

data = [
    {
        "name": "Flora",
        "itemStyle": {"color": "#da0d68"},
        "children": [
            {"name": "Black Tea", "value": 1, "itemStyle": {"color": "#975e6d"}},
            {
                "name": "Floral",
                "itemStyle": {"color": "#e0719c"},
                "children": [
                    {
                        "name": "Chamomile",
                        "value": 1,
                        "itemStyle": {"color": "#f99e1c"},
                    },
                    {"name": "Rose", "value": 1, "itemStyle": {"color": "#ef5a78"}},
                    {"name": "Jasmine", "value": 1, "itemStyle": {"color": "#f7f1bd"}},
                ],
            },
        ],
    },
    {
        "name": "Fruity",
        "itemStyle": {"color": "#da1d23"},
        "children": [
            {
                "name": "Berry",
                "itemStyle": {"color": "#dd4c51"},
                "children": [
                    {
                        "name": "Blackberry",
                        "value": 1,
                        "itemStyle": {"color": "#3e0317"},
                    },
                    {
                        "name": "Raspberry",
                        "value": 1,
                        "itemStyle": {"color": "#e62969"},
                    },
                    {
                        "name": "Blueberry",
                        "value": 1,
                        "itemStyle": {"color": "#6569b0"},
                    },
                    {
                        "name": "Strawberry",
                        "value": 1,
                        "itemStyle": {"color": "#ef2d36"},
                    },
                ],
            },
            {
                "name": "Dried Fruit",
                "itemStyle": {"color": "#c94a44"},
                "children": [
                    {"name": "Raisin", "value": 1, "itemStyle": {"color": "#b53b54"}},
                    {"name": "Prune", "value": 1, "itemStyle": {"color": "#a5446f"}},
                ],
            },
            {
                "name": "Other Fruit",
                "itemStyle": {"color": "#dd4c51"},
                "children": [
                    {"name": "Coconut", "value": 1, "itemStyle": {"color": "#f2684b"}},
                    {"name": "Cherry", "value": 1, "itemStyle": {"color": "#e73451"}},
                    {
                        "name": "Pomegranate",
                        "value": 1,
                        "itemStyle": {"color": "#e65656"},
                    },
                    {
                        "name": "Pineapple",
                        "value": 1,
                        "itemStyle": {"color": "#f89a1c"},
                    },
                    {"name": "Grape", "value": 1, "itemStyle": {"color": "#aeb92c"}},
                    {"name": "Apple", "value": 1, "itemStyle": {"color": "#4eb849"}},
                    {"name": "Peach", "value": 1, "itemStyle": {"color": "#f68a5c"}},
                    {"name": "Pear", "value": 1, "itemStyle": {"color": "#baa635"}},
                ],
            },
            {
                "name": "Citrus Fruit",
                "itemStyle": {"color": "#f7a128"},
                "children": [
                    {
                        "name": "Grapefruit",
                        "value": 1,
                        "itemStyle": {"color": "#f26355"},
                    },
                    {"name": "Orange", "value": 1, "itemStyle": {"color": "#e2631e"}},
                    {"name": "Lemon", "value": 1, "itemStyle": {"color": "#fde404"}},
                    {"name": "Lime", "value": 1, "itemStyle": {"color": "#7eb138"}},
                ],
            },
        ],
    },
    {
        "name": "Sour/\nFermented",
        "itemStyle": {"color": "#ebb40f"},
        "children": [
            {
                "name": "Sour",
                "itemStyle": {"color": "#e1c315"},
                "children": [
                    {
                        "name": "Sour Aromatics",
                        "value": 1,
                        "itemStyle": {"color": "#9ea718"},
                    },
                    {
                        "name": "Acetic Acid",
                        "value": 1,
                        "itemStyle": {"color": "#94a76f"},
                    },
                    {
                        "name": "Butyric Acid",
                        "value": 1,
                        "itemStyle": {"color": "#d0b24f"},
                    },
                    {
                        "name": "Isovaleric Acid",
                        "value": 1,
                        "itemStyle": {"color": "#8eb646"},
                    },
                    {
                        "name": "Citric Acid",
                        "value": 1,
                        "itemStyle": {"color": "#faef07"},
                    },
                    {
                        "name": "Malic Acid",
                        "value": 1,
                        "itemStyle": {"color": "#c1ba07"},
                    },
                ],
            },
            {
                "name": "Alcohol/\nFremented",
                "itemStyle": {"color": "#b09733"},
                "children": [
                    {"name": "Winey", "value": 1, "itemStyle": {"color": "#8f1c53"}},
                    {"name": "Whiskey", "value": 1, "itemStyle": {"color": "#b34039"}},
                    {
                        "name": "Fremented",
                        "value": 1,
                        "itemStyle": {"color": "#ba9232"},
                    },
                    {"name": "Overripe", "value": 1, "itemStyle": {"color": "#8b6439"}},
                ],
            },
        ],
    },
    {
        "name": "Green/\nVegetative",
        "itemStyle": {"color": "#187a2f"},
        "children": [
            {"name": "Olive Oil", "value": 1, "itemStyle": {"color": "#a2b029"}},
            {"name": "Raw", "value": 1, "itemStyle": {"color": "#718933"}},
            {
                "name": "Green/\nVegetative",
                "itemStyle": {"color": "#3aa255"},
                "children": [
                    {
                        "name": "Under-ripe",
                        "value": 1,
                        "itemStyle": {"color": "#a2bb2b"},
                    },
                    {"name": "Peapod", "value": 1, "itemStyle": {"color": "#62aa3c"}},
                    {"name": "Fresh", "value": 1, "itemStyle": {"color": "#03a653"}},
                    {
                        "name": "Dark Green",
                        "value": 1,
                        "itemStyle": {"color": "#038549"},
                    },
                    {
                        "name": "Vegetative",
                        "value": 1,
                        "itemStyle": {"color": "#28b44b"},
                    },
                    {"name": "Hay-like", "value": 1, "itemStyle": {"color": "#a3a830"}},
                    {
                        "name": "Herb-like",
                        "value": 1,
                        "itemStyle": {"color": "#7ac141"},
                    },
                ],
            },
            {"name": "Beany", "value": 1, "itemStyle": {"color": "#5e9a80"}},
        ],
    },
    {
        "name": "Other",
        "itemStyle": {"color": "#0aa3b5"},
        "children": [
            {
                "name": "Papery/Musty",
                "itemStyle": {"color": "#9db2b7"},
                "children": [
                    {"name": "Stale", "value": 1, "itemStyle": {"color": "#8b8c90"}},
                    {
                        "name": "Cardboard",
                        "value": 1,
                        "itemStyle": {"color": "#beb276"},
                    },
                    {"name": "Papery", "value": 1, "itemStyle": {"color": "#fefef4"}},
                    {"name": "Woody", "value": 1, "itemStyle": {"color": "#744e03"}},
                    {
                        "name": "Moldy/Damp",
                        "value": 1,
                        "itemStyle": {"color": "#a3a36f"},
                    },
                    {
                        "name": "Musty/Dusty",
                        "value": 1,
                        "itemStyle": {"color": "#c9b583"},
                    },
                    {
                        "name": "Musty/Earthy",
                        "value": 1,
                        "itemStyle": {"color": "#978847"},
                    },
                    {"name": "Animalic", "value": 1, "itemStyle": {"color": "#9d977f"}},
                    {
                        "name": "Meaty Brothy",
                        "value": 1,
                        "itemStyle": {"color": "#cc7b6a"},
                    },
                    {"name": "Phenolic", "value": 1, "itemStyle": {"color": "#db646a"}},
                ],
            },
            {
                "name": "Chemical",
                "itemStyle": {"color": "#76c0cb"},
                "children": [
                    {"name": "Bitter", "value": 1, "itemStyle": {"color": "#80a89d"}},
                    {"name": "Salty", "value": 1, "itemStyle": {"color": "#def2fd"}},
                    {
                        "name": "Medicinal",
                        "value": 1,
                        "itemStyle": {"color": "#7a9bae"},
                    },
                    {
                        "name": "Petroleum",
                        "value": 1,
                        "itemStyle": {"color": "#039fb8"},
                    },
                    {"name": "Skunky", "value": 1, "itemStyle": {"color": "#5e777b"}},
                    {"name": "Rubber", "value": 1, "itemStyle": {"color": "#120c0c"}},
                ],
            },
        ],
    },
    {
        "name": "Roasted",
        "itemStyle": {"color": "#c94930"},
        "children": [
            {"name": "Pipe Tobacco", "value": 1, "itemStyle": {"color": "#caa465"}},
            {"name": "Tobacco", "value": 1, "itemStyle": {"color": "#dfbd7e"}},
            {
                "name": "Burnt",
                "itemStyle": {"color": "#be8663"},
                "children": [
                    {"name": "Acrid", "value": 1, "itemStyle": {"color": "#b9a449"}},
                    {"name": "Ashy", "value": 1, "itemStyle": {"color": "#899893"}},
                    {"name": "Smoky", "value": 1, "itemStyle": {"color": "#a1743b"}},
                    {
                        "name": "Brown, Roast",
                        "value": 1,
                        "itemStyle": {"color": "#894810"},
                    },
                ],
            },
            {
                "name": "Cereal",
                "itemStyle": {"color": "#ddaf61"},
                "children": [
                    {"name": "Grain", "value": 1, "itemStyle": {"color": "#b7906f"}},
                    {"name": "Malt", "value": 1, "itemStyle": {"color": "#eb9d5f"}},
                ],
            },
        ],
    },
    {
        "name": "Spices",
        "itemStyle": {"color": "#ad213e"},
        "children": [
            {"name": "Pungent", "value": 1, "itemStyle": {"color": "#794752"}},
            {"name": "Pepper", "value": 1, "itemStyle": {"color": "#cc3d41"}},
            {
                "name": "Brown Spice",
                "itemStyle": {"color": "#b14d57"},
                "children": [
                    {"name": "Anise", "value": 1, "itemStyle": {"color": "#c78936"}},
                    {"name": "Nutmeg", "value": 1, "itemStyle": {"color": "#8c292c"}},
                    {"name": "Cinnamon", "value": 1, "itemStyle": {"color": "#e5762e"}},
                    {"name": "Clove", "value": 1, "itemStyle": {"color": "#a16c5a"}},
                ],
            },
        ],
    },
    {
        "name": "Nutty/\nCocoa",
        "itemStyle": {"color": "#a87b64"},
        "children": [
            {
                "name": "Nutty",
                "itemStyle": {"color": "#c78869"},
                "children": [
                    {"name": "Peanuts", "value": 1, "itemStyle": {"color": "#d4ad12"}},
                    {"name": "Hazelnut", "value": 1, "itemStyle": {"color": "#9d5433"}},
                    {"name": "Almond", "value": 1, "itemStyle": {"color": "#c89f83"}},
                ],
            },
            {
                "name": "Cocoa",
                "itemStyle": {"color": "#bb764c"},
                "children": [
                    {
                        "name": "Chocolate",
                        "value": 1,
                        "itemStyle": {"color": "#692a19"},
                    },
                    {
                        "name": "Dark Chocolate",
                        "value": 1,
                        "itemStyle": {"color": "#470604"},
                    },
                ],
            },
        ],
    },
    {
        "name": "Sweet",
        "itemStyle": {"color": "#e65832"},
        "children": [
            {
                "name": "Brown Sugar",
                "itemStyle": {"color": "#d45a59"},
                "children": [
                    {"name": "Molasses", "value": 1, "itemStyle": {"color": "#310d0f"}},
                    {
                        "name": "Maple Syrup",
                        "value": 1,
                        "itemStyle": {"color": "#ae341f"},
                    },
                    {
                        "name": "Caramelized",
                        "value": 1,
                        "itemStyle": {"color": "#d78823"},
                    },
                    {"name": "Honey", "value": 1, "itemStyle": {"color": "#da5c1f"}},
                ],
            },
            {"name": "Vanilla", "value": 1, "itemStyle": {"color": "#f89a80"}},
            {"name": "Vanillin", "value": 1, "itemStyle": {"color": "#f37674"}},
            {"name": "Overall Sweet", "value": 1, "itemStyle": {"color": "#e75b68"}},
            {"name": "Sweet Aromatics", "value": 1, "itemStyle": {"color": "#d0545f"}},
        ],
    },
]

c = (
	Sunburst(init_opts = opts.InitOpts(width = "1000px",height = "600px"))
	.add(
		"",
		data_pair = data,
		highlight_policy = "ancestor",
		radius = [0,"95%"],
		sort_ = "null",
		levels = [
			{},
			{
				"r0":"15%",
				"r":"35%",
				"itemStyle":{"borderWidth":2},
				"label":{"rotate":"tangential"}
			},
			{
				"r0":"35%",
				"r":"70%",
				"label":{"align":"right"},
			},
			{
				"r0":"70%",
				"r":"72%",
				"label":{"position":"outside","padding":3},
				"itemStyle":{"borderWidth":3},
			},

		],
		)
	.set_global_opts(title_opts = opts.TitleOpts(title = "Sunburst示例"))
	.set_series_opts(label_opts = opts.LabelOpts(formatter = "{b}"))
	.render("drink_flavors.html")

	)

#Section3 主题河流图
from pyecharts.charts import ThemeRiver
series_data = ["DQ", "TY", "SS", "QG", "SY", "DD"]
data = [
    ["2015/11/08", 10, "DQ"],
    ["2015/11/09", 15, "DQ"],
    ["2015/11/10", 35, "DQ"],
    ["2015/11/11", 38, "DQ"],
    ["2015/11/12", 22, "DQ"],
    ["2015/11/13", 16, "DQ"],
    ["2015/11/14", 7, "DQ"],
    ["2015/11/15", 2, "DQ"],
    ["2015/11/16", 17, "DQ"],
    ["2015/11/17", 33, "DQ"],
    ["2015/11/18", 40, "DQ"],
    ["2015/11/19", 32, "DQ"],
    ["2015/11/20", 26, "DQ"],
    ["2015/11/21", 35, "DQ"],
    ["2015/11/22", 40, "DQ"],
    ["2015/11/23", 32, "DQ"],
    ["2015/11/24", 26, "DQ"],
    ["2015/11/25", 22, "DQ"],
    ["2015/11/26", 16, "DQ"],
    ["2015/11/27", 22, "DQ"],
    ["2015/11/28", 10, "DQ"],
    ["2015/11/08", 35, "TY"],
    ["2015/11/09", 36, "TY"],
    ["2015/11/10", 37, "TY"],
    ["2015/11/11", 22, "TY"],
    ["2015/11/12", 24, "TY"],
    ["2015/11/13", 26, "TY"],
    ["2015/11/14", 34, "TY"],
    ["2015/11/15", 21, "TY"],
    ["2015/11/16", 18, "TY"],
    ["2015/11/17", 45, "TY"],
    ["2015/11/18", 32, "TY"],
    ["2015/11/19", 35, "TY"],
    ["2015/11/20", 30, "TY"],
    ["2015/11/21", 28, "TY"],
    ["2015/11/22", 27, "TY"],
    ["2015/11/23", 26, "TY"],
    ["2015/11/24", 15, "TY"],
    ["2015/11/25", 30, "TY"],
    ["2015/11/26", 35, "TY"],
    ["2015/11/27", 42, "TY"],
    ["2015/11/28", 42, "TY"],
    ["2015/11/08", 21, "SS"],
    ["2015/11/09", 25, "SS"],
    ["2015/11/10", 27, "SS"],
    ["2015/11/11", 23, "SS"],
    ["2015/11/12", 24, "SS"],
    ["2015/11/13", 21, "SS"],
    ["2015/11/14", 35, "SS"],
    ["2015/11/15", 39, "SS"],
    ["2015/11/16", 40, "SS"],
    ["2015/11/17", 36, "SS"],
    ["2015/11/18", 33, "SS"],
    ["2015/11/19", 43, "SS"],
    ["2015/11/20", 40, "SS"],
    ["2015/11/21", 34, "SS"],
    ["2015/11/22", 28, "SS"],
    ["2015/11/23", 26, "SS"],
    ["2015/11/24", 37, "SS"],
    ["2015/11/25", 41, "SS"],
    ["2015/11/26", 46, "SS"],
    ["2015/11/27", 47, "SS"],
    ["2015/11/28", 41, "SS"],
    ["2015/11/08", 10, "QG"],
    ["2015/11/09", 15, "QG"],
    ["2015/11/10", 35, "QG"],
    ["2015/11/11", 38, "QG"],
    ["2015/11/12", 22, "QG"],
    ["2015/11/13", 16, "QG"],
    ["2015/11/14", 7, "QG"],
    ["2015/11/15", 2, "QG"],
    ["2015/11/16", 17, "QG"],
    ["2015/11/17", 33, "QG"],
    ["2015/11/18", 40, "QG"],
    ["2015/11/19", 32, "QG"],
    ["2015/11/20", 26, "QG"],
    ["2015/11/21", 35, "QG"],
    ["2015/11/22", 40, "QG"],
    ["2015/11/23", 32, "QG"],
    ["2015/11/24", 26, "QG"],
    ["2015/11/25", 22, "QG"],
    ["2015/11/26", 16, "QG"],
    ["2015/11/27", 22, "QG"],
    ["2015/11/28", 10, "QG"],
    ["2015/11/08", 10, "SY"],
    ["2015/11/09", 15, "SY"],
    ["2015/11/10", 35, "SY"],
    ["2015/11/11", 38, "SY"],
    ["2015/11/12", 22, "SY"],
    ["2015/11/13", 16, "SY"],
    ["2015/11/14", 7, "SY"],
    ["2015/11/15", 2, "SY"],
    ["2015/11/16", 17, "SY"],
    ["2015/11/17", 33, "SY"],
    ["2015/11/18", 40, "SY"],
    ["2015/11/19", 32, "SY"],
    ["2015/11/20", 26, "SY"],
    ["2015/11/21", 35, "SY"],
    ["2015/11/22", 4, "SY"],
    ["2015/11/23", 32, "SY"],
    ["2015/11/24", 26, "SY"],
    ["2015/11/25", 22, "SY"],
    ["2015/11/26", 16, "SY"],
    ["2015/11/27", 22, "SY"],
    ["2015/11/28", 10, "SY"],
    ["2015/11/08", 10, "DD"],
    ["2015/11/09", 15, "DD"],
    ["2015/11/10", 35, "DD"],
    ["2015/11/11", 38, "DD"],
    ["2015/11/12", 22, "DD"],
    ["2015/11/13", 16, "DD"],
    ["2015/11/14", 7, "DD"],
    ["2015/11/15", 2, "DD"],
    ["2015/11/16", 17, "DD"],
    ["2015/11/17", 33, "DD"],
    ["2015/11/18", 4, "DD"],
    ["2015/11/19", 32, "DD"],
    ["2015/11/20", 26, "DD"],
    ["2015/11/21", 35, "DD"],
    ["2015/11/22", 40, "DD"],
    ["2015/11/23", 32, "DD"],
    ["2015/11/24", 26, "DD"],
    ["2015/11/25", 22, "DD"],
    ["2015/11/26", 16, "DD"],
    ["2015/11/27", 22, "DD"],
    ["2015/11/28", 10, "DD"],
]

c = (
	ThemeRiver(init_opts = opts.InitOpts(width = "1600px",height = "800px"))
	.add(
		series_name = series_data,
		data = data,
		singleaxis_opts = opts.SingleAxisOpts(
			pos_top = "50",
			pos_bottom = "50",
			type_ = "time",
			)
		)
	.set_global_opts(
		tooltip_opts = opts.TooltipOpts(trigger = "axis",axis_pointer_type = "line")
		)
	.render("theme_river.html")


	)

# Section4 词云图
from pyecharts.charts import WordCloud
data = [
    ("生活资源", "999"),
    ("供热管理", "888"),
    ("供气质量", "777"),
    ("生活用水管理", "688"),
    ("一次供水问题", "588"),
    ("交通运输", "516"),
    ("城市交通", "515"),
    ("环境保护", "483"),
    ("房地产管理", "462"),
    ("城乡建设", "449"),
    ("社会保障与福利", "429"),
    ("社会保障", "407"),
    ("文体与教育管理", "406"),
    ("公共安全", "406"),
    ("公交运输管理", "386"),
    ("出租车运营管理", "385"),
    ("供热管理", "375"),
    ("市容环卫", "355"),
    ("自然资源管理", "355"),
    ("粉尘污染", "335"),
    ("噪声污染", "324"),
    ("土地资源管理", "304"),
    ("物业服务与管理", "304"),
    ("医疗卫生", "284"),
    ("粉煤灰污染", "284"),
    ("占道", "284"),
    ("供热发展", "254"),
    ("农村土地规划管理", "254"),
    ("生活噪音", "253"),
    ("供热单位影响", "253"),
    ("城市供电", "223"),
    ("房屋质量与安全", "223"),
    ("大气污染", "223"),
    ("房屋安全", "223"),
    ("文化活动", "223"),
    ("拆迁管理", "223"),
    ("公共设施", "223"),
    ("供气质量", "223"),
    ("供电管理", "223"),
    ("燃气管理", "152"),
    ("教育管理", "152"),
    ("医疗纠纷", "152"),
    ("执法监督", "152"),
    ("设备安全", "152"),
    ("政务建设", "152"),
    ("县区、开发区", "152"),
    ("宏观经济", "152"),
    ("教育管理", "112"),
    ("社会保障", "112"),
    ("生活用水管理", "112"),
    ("物业服务与管理", "112"),
    ("分类列表", "112"),
    ("农业生产", "112"),
    ("二次供水问题", "112"),
    ("城市公共设施", "92"),
    ("拆迁政策咨询", "92"),
    ("物业服务", "92"),
    ("物业管理", "92"),
    ("社会保障保险管理", "92"),
    ("低保管理", "92"),
    ("文娱市场管理", "72"),
    ("城市交通秩序管理", "72"),
    ("执法争议", "72"),
    ("商业烟尘污染", "72"),
    ("占道堆放", "71"),
    ("地上设施", "71"),
    ("水质", "71"),
    ("无水", "71"),
    ("供热单位影响", "71"),
    ("人行道管理", "71"),
    ("主网原因", "71"),
    ("集中供热", "71"),
    ("客运管理", "71"),
    ("国有公交（大巴）管理", "71"),
    ("工业粉尘污染", "71"),
    ("治安案件", "71"),
    ("压力容器安全", "71"),
    ("身份证管理", "71"),
    ("群众健身", "41"),
    ("工业排放污染", "41"),
    ("破坏森林资源", "41"),
    ("市场收费", "41"),
    ("生产资金", "41"),
    ("生产噪声", "41"),
    ("农村低保", "41"),
    ("劳动争议", "41"),
    ("劳动合同争议", "41"),
    ("劳动报酬与福利", "41"),
    ("医疗事故", "21"),
    ("停供", "21"),
    ("基础教育", "21"),
    ("职业教育", "21"),
    ("物业资质管理", "21"),
    ("拆迁补偿", "21"),
    ("设施维护", "21"),
    ("市场外溢", "11"),
    ("占道经营", "11"),
    ("树木管理", "11"),
    ("农村基础设施", "11"),
    ("无水", "11"),
    ("供气质量", "11"),
    ("停气", "11"),
    ("市政府工作部门（含部门管理机构、直属单位）", "11"),
    ("燃气管理", "11"),
    ("市容环卫", "11"),
    ("新闻传媒", "11"),
    ("人才招聘", "11"),
    ("市场环境", "11"),
    ("行政事业收费", "11"),
    ("食品安全与卫生", "11"),
    ("城市交通", "11"),
    ("房地产开发", "11"),
    ("房屋配套问题", "11"),
    ("物业服务", "11"),
    ("物业管理", "11"),
    ("占道", "11"),
    ("园林绿化", "11"),
    ("户籍管理及身份证", "11"),
    ("公交运输管理", "11"),
    ("公路（水路）交通", "11"),
    ("房屋与图纸不符", "11"),
    ("有线电视", "11"),
    ("社会治安", "11"),
    ("林业资源", "11"),
    ("其他行政事业收费", "11"),
    ("经营性收费", "11"),
    ("食品安全与卫生", "11"),
    ("体育活动", "11"),
    ("有线电视安装及调试维护", "11"),
    ("低保管理", "11"),
    ("劳动争议", "11"),
    ("社会福利及事务", "11"),
    ("一次供水问题", "11"),
]

c = (
	WordCloud()
	.add(
		series_name = "热点分析",data_pair = data,word_size_range = [6,66],
		)
	.set_global_opts(
		title_opts = opts.TitleOpts(title = "热点分析",title_textstyle_opts = opts.TextStyleOpts(font_size = 23)),
		tooltip_opts = opts.TooltipOpts(is_show = True),
		)
	.render("basic_wordcloud.html")

	)















