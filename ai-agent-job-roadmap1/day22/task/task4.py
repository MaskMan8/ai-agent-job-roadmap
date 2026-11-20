import pandas as pd

orders_df = pd.read_csv("orders.csv",encoding="UTF8")
#pandas去重
unique_orders = orders_df.drop_duplicates(subset="order_id",keep="first")
#给去重的订单新增两个列
unique_orders["unit_price_num"] = pd.to_numeric(unique_orders["unit_price"], errors="coerce")
unique_orders["quantity_num"] = pd.to_numeric(unique_orders["quantity"], errors="coerce")
#筛选出符合条件的订单
valid_mask = (unique_orders["quantity_num"]>0)&(unique_orders["unit_price_num"]>0)
valid_orders = unique_orders[valid_mask].copy()
print(valid_orders)
#用pandas计算有效订单的销售额
sales = (valid_orders["quantity_num"]*valid_orders["unit_price_num"])
valid_orders["sales"] = sales

print(valid_orders[["order_id","city","quantity_num","unit_price_num","sales"]])
print(valid_orders["sales"].sum())


#业务需求：统计每个城市的销售额，找出销售贡献最高的城市

valid_orders_city = valid_orders.groupby("city")




