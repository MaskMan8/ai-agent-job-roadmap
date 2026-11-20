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
                    review_reasons.append("待确认")
                

        row_number = index + 2
        order_id = row["order_id"]
        
        print(f"CSV行号:{row_number}，订单编号：{order_id}")
        print(f"异常原因：{errors}")
        print(f"待确认原因：{review_reasons}")

    print(seen_order_ids)    

with open("orders.csv","r",encoding="UTF8",newline="") as f:
         orders_df = pd.read_csv(f)

validate_orders(orders_df)
