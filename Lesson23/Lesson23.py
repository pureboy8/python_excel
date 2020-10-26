import json
from pyecharts.charts import BMap
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


# 安装chrome浏览器
# 查看chrome浏览器版本
# 到 http://chromedriver.storage.googleapis.com/index.html 去下载对应的chromedriver
# mac 
# 把chromedriver 拖到/usr/bin/文件夹下
# window 
# 将其解压在chrome的安装目录下(C:\Program Files (x86)\Google\Chrome\Application\)
# 1. 进入我的电脑->属性->高级系统设置->环境变量
# 2. 修改path在最后面添加 ;C:\Program Files (x86)\Google\Chrome\Application\
# pip install snapshot_selenium
# pip3 install snapshot_selenium

with open("config.json","r") as f:
    config = json.load(f)

BAIDU_MAP_AK = config["BAIDU_MAP_AK"]
# BAIDU_MAP_AK = "FAKE_AK"

# 读取项目中的 json 文件
with open("busRoutines.json", "r", encoding="utf-8") as f:
    bus_lines = json.load(f)



c = (
    BMap(init_opts=opts.InitOpts(width="1920px", height="1080px",theme = ThemeType.DARK))
    .add_schema(
        baidu_ak=BAIDU_MAP_AK,
        center=[116.40, 40.04],
        zoom=10,
        is_roam=True,
        map_style={
            "styleJson": [
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {"color": "#031628"},
                },
                {
                    "featureType": "land",
                    "elementType": "geometry",
                    "stylers": {"color": "#000102"},
                },
                {
                    "featureType": "highway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.stroke",
                    "stylers": {"color": "#0b3d51"},
                },
                {
                    "featureType": "local",
                    "elementType": "geometry",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "railway",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "railway",
                    "elementType": "geometry.stroke",
                    "stylers": {"color": "#08304b"},
                },
                {
                    "featureType": "subway",
                    "elementType": "geometry",
                    "stylers": {"lightness": -70},
                },
                {
                    "featureType": "building",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": {"color": "#857f7f"},
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.stroke",
                    "stylers": {"color": "#000000"},
                },
                {
                    "featureType": "building",
                    "elementType": "geometry",
                    "stylers": {"color": "#022338"},
                },
                {
                    "featureType": "green",
                    "elementType": "geometry",
                    "stylers": {"color": "#062032"},
                },
                {
                    "featureType": "boundary",
                    "elementType": "all",
                    "stylers": {"color": "#465b6c"},
                },
                {
                    "featureType": "manmade",
                    "elementType": "all",
                    "stylers": {"color": "#022338"},
                },
                {
                    "featureType": "label",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
            ]
        },
    )
    .add(
        "",
        type_="lines",
        is_polyline=True,
        data_pair=bus_lines,
        linestyle_opts=opts.LineStyleOpts(opacity=0.2, width=0.5),
    )
    .set_global_opts(title_opts = opts.TitleOpts(title = "北京公交车运营路线图",pos_left = "0"))
    .render("bmap_beijing_bus_routines.html")
)

make_snapshot(snapshot,c,"c.png")
