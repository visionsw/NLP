import numpy
import pandas
dataframe0 = pandas.read_excel(r"D:/data4hw2.xlsx", sheet_name=0, header=0)
# 使用isnull函数检测dataframe0中缺失的数据
dataframe0.isnull()
# 删除dataframe0中“age”列数据为空的行
dataframe1 = dataframe0
print("---------dataframe1---------")
print(dataframe1.dropna(subset=["age"]))
#删除dataframe0中所有的含有空值的行
dataframe2 = dataframe0
print("---------dataframe2---------")
print(dataframe2.dropna(axis=0,how="any"))
#将dataframe0中所有的空值替换为数字0
dataframe3 = dataframe0
print("---------dataframe3---------")
print(dataframe3.fillna(value=0))


