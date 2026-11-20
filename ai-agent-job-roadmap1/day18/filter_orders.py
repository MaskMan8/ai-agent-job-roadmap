import os
import csv

print("当前工作目录：", os.getcwd())
print("文件是否存在：", os.path.exists("orders.csv"))

orders = []
filtered_orders = []
with open("orders.csv","r",encoding = "UTF8",newline = "") as f:
    csv_dictreader = csv.DictReader(f)
    for row in csv_dictreader:
        orders.append(row)
        
    target_city = input("输入你要查询的城市")
    for order in orders:
        city = order["city"]
        if city == target_city:
            print(order)
            filtered_orders.append(order)

    print(f"符合条件的订单数{len(filtered_orders)}")
    if len(filtered_orders) == 0:
        print("没有找到该城市的订单")
    else:
        print("找到了订单！")