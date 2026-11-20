
import pandas as pd

orders_df = pd.read_csv("orders.csv", encoding="UTF8")

# 1. 转换数量
orders_df["quantity_num"] = pd.to_numeric(
    orders_df["quantity"],
    errors="coerce"
)

# 2. 转换单价
orders_df["unit_price_num"] = pd.to_numeric(
    orders_df["unit_price"],
    errors="coerce"
)

# 3. 查看转换结果
print(orders_df[
    ["order_id", "quantity", "quantity_num",
     "unit_price", "unit_price_num"]
])
