import pandas as pd

print(pd.__version__)

orders_df = pd.read_csv("orders.csv", encoding="UTF8")
#查看规模
print(orders_df.shape)
#查看前几行数据
print(orders_df.head())
#查看数据类型
print(type(orders_df))
#查看列名
print(orders_df.columns)