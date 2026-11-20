import pandas as pd

def load_orders(file_path):
    
    required_fields = [
    "order_id",
    "product",
    "quantity",
    "unit_price",
    "city"
    ]
    
    try:
        with open(file_path,"r",encoding="UTF8",newline="") as f:
            orders_df = pd.read_csv(f)
            missing_header = set(required_fields)-set(orders_df.columns)
            if missing_header:
                print(f"缺少必要的表头字段: {missing_header}")
                return None
            else:
                return orders_df
    except FileNotFoundError:
        print("文件不存在")
        return None

orders_df = load_orders("orders.csv")
print(orders_df)