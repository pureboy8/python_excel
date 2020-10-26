# Section0 开场
print("-"*30 + "Begin Section 0 开场" + "-"*30)
print("这是Python的第二十一次课程,主要讲数据可视化:")
print("树图")
print("-"*30 + "End Section 0 开场" + "-"*30)
print('\n')

#Section1
from pyecharts.charts import Tree
from pyecharts import options as opts
from pyecharts.globals import ThemeType 
data = [
    {
        "name":"中国",
        "value":140005,
        "children":[
            {
                "name":"广东",
                "value":11169,
                "children":[
                    {"name":"广州","value":1490},
                    {"name":"深圳","value":1302},
                    {"name":"东莞","value":839},
                    {"name":"佛山","value":790},
                    {"name":"湛江","value":733},

                ]            
            },
            {
                "name":"山东",
                "value":10005,
                "children":[
                    {"name":"临沂","value":1066},
                    {"name":"青岛","value":949},
                    {"name":"潍坊","value":935},
                    {"name":"济南","value":890},
                    {"name":"菏泽","value":878},
                ]
            },
            {
                "name":"河南",
                "value":9559,
                "children":[
                    {"name":"南阳","value":1002},
                    {"name":"郑州","value":956},
                    {"name":"周口","value":880},
                    {"name":"商丘","value":727},
                    {"name":"驻马店","value":695}
                ]
            },
            {
                "name":"四川",
                "value":8302,
                "children":[
                    {"name":"成都","value":1658},
                    {"name":"南充","value":643},
                    {"name":"达州","value":574},
                    {"name":"绵阳","value":487},
                    {"name":"宜宾","value":457},
                ]
            },
            {
                "name":"江苏",
                "value":8029,
                "children":[
                    {"name":"苏州","value":1074},
                    {"name":"徐州","value":882},
                    {"name":"南京","value":850},
                    {"name":"南通","value":731},
                    {"name":"盐城","value":720},
                ]
            },
            {
                "name":"河北",
                "value":7519,
                "children":[
                    {"name":"保定","value":1042},
                    {"name":"石家庄","value":1015},
                    {"name":"邯郸","value":949},
                    {"name":"唐山","value":784},
                    {"name":"沧州","value":750}
                ]
            },
            {
                "name":"湖南",
                "value":6860,
                "children":[
                    {"name":"长沙","value":731},
                    {"name":"衡阳","value":730},
                    {"name":"邵阳","value":721},
                    {"name":"常德","value":583},
                    {"name":"岳阳","value":559}
                ]
            },
            {
                "name":"安徽",
                "value":6254,
                "children":[
                    {"name":"阜阳","value":820},
                    {"name":"合肥","value":808},
                    {"name":"宿州","value":568},
                    {"name":"亳州","value":523},
                    {"name":"六安","value":483},
                ]
            },
            {
                "name":"湖北",
                "value":5902,
                "children":[
                    {"name":"武汉","value":1060},
                    {"name":"黄冈","value":629},
                    {"name":"荆州","value":574},
                    {"name":"襄阳","value":561},
                    {"name":"孝感","value":487},
                ]
            },
            {
                "name":"浙江",
                "value":5657,
                "children":[
                    {"name":"杭州","value":918},
                    {"name":"温州","value":917},
                    {"name":"宁波","value":787},
                    {"name":"台州","value":608},
                    {"name":"金华","value":552},
                ]
            }

        ],
        # "hoverAnimation","symbolSize","lineStyle"...

    }

]

colors=[
    "#00ADD0",
    "#FFA12F",
    "#B62AFF",
    "#604BFF",
    "#6E35FF",
    "#002AFF",
    "#20C0F4",
    "#95F300",
    "#04FDB8",
    "#AF5AFF"
]

# 为了实现每个层次的item样式不一样，而对data数据再处理
def handleData(data,index,color = "#00f6ff"):
    for index2 in range(len(data)):
        item = data[index2]
        item["hoverAnimation"] = True
        if index == 1:
            color = colors[index2 % 10]
        # 设置节点的标签位置
        if index == 0 or index == 1:
            item["label"] = {
                "position":"inside",
            }
        # 设置节点的大小
        if index == 0:
            item["symbolSize"] = 70
        elif index == 1:
            item["symbolSize"] = 50
        else:
            item["symbolSize"] = 10
        # 设置线条颜色
        item["lineStyle"] = {"color" : color}

        if "children" in item:
            item["itemStyle"] = {
                "borderColor":color,
                "color":color,
            }
            item["children"] = handleData(item["children"],index+1,color)
        else:
            item["itemStyle"] = {
                "color":"transparent",
                "borderColor":color,
            }
        data[index2] = item
    return data

data1 = handleData(data,0)
print(data1)

c = (
    Tree(init_opts = opts.InitOpts(width = "1920px",height = "1080px",theme = ThemeType.DARK))
    .add(
        "",
        data = handleData(data,0),
        pos_top = 30,
        pos_bottom = 0,
        pos_left = 0,
        pos_right = 0,
        layout = "radial",
        symbol = "circle",
        symbol_size = 10,
        initial_tree_depth = 2,
        is_expand_and_collapse = True,
        itemstyle_opts = opts.ItemStyleOpts(border_width = 1),
        label_opts = opts.LabelOpts(
            color = "#fff",
            font_size = 10,
            position = "inside",
            font_family = "SourceHanSansCN",
            rotate = 0
            ),
        tooltip_opts = opts.TooltipOpts(
            trigger = "item",
            trigger_on = "mousemove",
            background_color = "rgba(1,70,86,1)",
            border_color = "rgba(0,246,255,1)",
            border_width = 0.5,
            textstyle_opts = opts.TextStyleOpts(font_size = 10),
            )
        )
    .set_global_opts(
        title_opts = opts.TitleOpts(title = "2019年常驻人口数前十的省份及城市（单位：万人）"),

        )
    .render("2019_china_population.html")


    )




