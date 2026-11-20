import pandas as pd
#读取csv文件并将格式转化为DataFrame
orders_df = pd.read_csv("orders.csv")
#查找单列
products = orders_df["product"]
#选择多列
selected_orders = orders_df[["order_id","product","city"]]
#杭州订单筛选
hangzhou_orders = orders_df[orders_df["city"] == "杭州"]

print(products)
print(selected_orders)
print(hangzhou_orders)
#分组统计杭州订单数量
city_count = orders_df.groupby("city").size()
print(city_count)
#分组统计产品数量
product_missing = (
    orders_df["product"].fillna("").str.strip() == ""
)

missing_orders = orders_df[product_missing]
print(missing_orders)
product_count = orders_df.groupby("product").size()
print(product_count)


