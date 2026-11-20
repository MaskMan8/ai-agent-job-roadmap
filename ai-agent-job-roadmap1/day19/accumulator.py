import csv
def orders_sales(order_quantity,order_price):
    return int(order_quantity)*float(order_price)

with open ("orders.csv","r",encoding = "UTF8",newline = "") as f:
    orders_data = csv.DictReader(f)
    
    total_sales = 0
    
    for row in orders_data:

        order_quantity = row["quantity"]
        order_price = row["unit_price"]
        order_product = row["product"]
        order_sales = orders_sales(order_quantity,order_price)

        print(f"当前产品：{order_product}")  
        print(f"{order_product}的数量是{order_quantity}")
        print(f"{order_product}的销售额是{order_sales}")
        print("")
   
        total_sales += order_sales
        
    print(f"所有订单的总销售额是{total_sales}")