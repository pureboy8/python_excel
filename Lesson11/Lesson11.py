# Section0 开场
print("-"*30 + "Begin Section 0 开场" + "-"*30)
print("这是Python的第十一次课程,主要讲数据汇总运算:")
print("1.求和\n2.求均值\n3.求最大值\n4.求最小值\n5.求中位数\n6.求众数\n7.求方差\n8.求标准差")
print("-"*30 + "End Section 0 开场" + "-"*30)
print('\n')

import pandas as pd
df = pd.read_excel(r"/Users/jack/Desktop/Python/Lesson11/Lesson11.xlsx");
print(df)

# 求和
# sum(),axis = 0,表示对列求和，axis=1表示对行求和
print("前25总财富：")
print(df["财富"].sum())


# 求均值
print("前25的财富均值：")
print(df["财富"].mean())

# 求最大值
print("前25的财富最大值：")
print(df["财富"].max())

# 求最小值
print("前25的财富最小值：")
print(df["财富"].min())

# 求中位数
print("前25的财富中位数：")
print(df["财富"].median())


# 求众数
print("前25的财富众数：")
print(df["财富"].mode())

# 求方差
print("前25的财富方差：")
print(df["财富"].var())

# 求标准差
print("前25的财富标准差：")
print(df["财富"].std())