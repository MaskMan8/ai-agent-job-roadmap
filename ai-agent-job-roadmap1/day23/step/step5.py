import pandas as pd

def validate_orders(orders_df):
    required_fields = [
    "order_id",
    "product",
    "quantity",
    "unit_price",
    "city"
   ]

    seen_order_ids = set()
    clean_orders = []
    error_logs = []
    review_orders = []

    for index,row in  orders_df.iterrows():

        errors = []
        review_reasons = []

        #检查必要字段
        for field in required_fields:
            value = row[field]

            if pd.isna(value):
                errors.append(f"缺少必要的字段: {field}")
            else:
                value = str(value).strip()
                if not value:
                    errors.append(f"字段为空: {field}")

        order_id = row["order_id"]
        #检查订单编号是否重复
        if not pd.isna(order_id):
            order_id = str(order_id).strip()
            if order_id:
                if order_id in seen_order_ids:
                    errors.append("订单编号重复")
                else:
                    seen_order_ids.add(order_id)
        # 商品数量合法性检查
        quantity = row["quantity"]
        if not pd.isna(quantity):
            quantity = str(quantity).strip()
            if quantity:
                quantity = pd.to_numeric(quantity, errors="coerce")
                if pd.isna(quantity):
                    errors.append("数量格式错误")
                elif quantity <= 0:
                    errors.append("数量必须大于0")
                elif quantity % 1 != 0:
                    errors.append("数量必须为整数")
        #商品单价合法性检查
        unit_price = row["unit_price"]
        if not pd.isna(unit_price):
            unit_price = str(unit_price).strip()
            if unit_price:
                unit_price = pd.to_numeric(unit_price,errors="coerce")
                if pd.isna(unit_price):
                    errors.append("价格格式错误")
                elif unit_price < 0:
                    errors.append("单价不能为负数")
                elif unit_price == 0:
                    review_reasons.append("零价格需要业务确认")


        row_number = index + 2
        order_id = row["order_id"]
        
        print(f"CSV行号:{row_number}，订单编号：{order_id}")
        print(f"异常原因：{errors}")
        print(f"待确认原因：{review_reasons}")

        row = row.to_dict()
        if errors:
            error_logs.append({"row_number": row_number, "order_id": order_id, "errors": errors,"raw_data": row })
        elif review_reasons:
            review_orders.append({"row_number": row_number, "order_id": order_id, "review_reasons": review_reasons,"raw_data": row })
        else:
            clean_orders.append(row)        
    print(seen_order_ids)    
    return clean_orders, error_logs, review_orders

with open("orders.csv","r",encoding="UTF8",newline="") as f:
         orders_df = pd.read_csv(f)

clean_orders, error_logs, review_orders = validate_orders(orders_df)
print(f"正常订单数量：{len(clean_orders)}")
print(f"异常订单数量：{len(error_logs)}")
print(f"待确认订单数量：{len(review_orders)}")

classified_total = (
    len(clean_orders)
    + len(error_logs)
    + len(review_orders)
)

print(f"分类后订单总数：{classified_total}")
print(f"原始订单总数：{len(orders_df)}")

if classified_total == len(orders_df):
    print("数量核对通过")
else:
    print("数量核对失败")

# 2. 将正常订单列表转换为 DataFrame
clean_df = pd.DataFrame(clean_orders)

# 3. 查看数据维度
print("\n===== 正常订单数据 =====")
print(clean_df.shape)

# 4. 查看前5条数据
print(clean_df.head())

# 计算每笔订单销售额
clean_df["quantity_num"] = pd.to_numeric(
    clean_df["quantity"], errors="coerce"
)

clean_df["unit_price_num"] = pd.to_numeric(
    clean_df["unit_price"], errors="coerce"
)

clean_df["sales"] = (
    clean_df["quantity_num"] * clean_df["unit_price_num"]
)

# 总销售额
total_sales = clean_df["sales"].sum()

# 城市销售额
city_sales = clean_df.groupby("city")["sales"].sum()

# 商品销售额
product_sales = clean_df.groupby("product")["sales"].sum()

# 销售额最高的城市
top_city = city_sales.idxmax()
max_city_sales = city_sales.max()

# 销售额最高的商品
top_product = product_sales.idxmax()
max_product_sales = product_sales.max()

# 输出结果
print(f"总销售额：{total_sales}")
print(f"销售额最高的城市：{top_city}，销售额：{max_city_sales}")
print(f"销售额最高的商品：{top_product}，销售额：{max_product_sales}")

# 1. 导出正常订单
clean_df.to_csv(
    "output/clean_orders.csv",
    index=False,
    encoding="utf-8-sig"
)

print("正常订单导出成功！")
print(f"导出订单数量：{len(clean_df)}")

# 2. 导出异常订单
error_df = pd.DataFrame(error_logs)
error_df.to_csv(
    "output/error_logs.csv",
    index=False,
    encoding="utf-8-sig"
)

# 3. 导出待确认订单
review_df = pd.DataFrame(review_orders)
review_df.to_csv(
    "output/review_orders.csv",
    index=False,
    encoding="utf-8-sig"
)

# 4. 导出城市销售额
city_sales.to_csv(
    "output/city_sales.csv",
    encoding="utf-8-sig"
)

# 5. 导出商品销售额
product_sales.to_csv(
    "output/product_sales.csv",
    encoding="utf-8-sig"
)

print("所有分析结果导出完成！")
