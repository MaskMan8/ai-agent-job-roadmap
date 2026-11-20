import csv

#单笔销售额
def order_sales(quantity,unit_price):
    order_sales = int(quantity)*float(unit_price)
    return order_sales

#打开文件读取字典数据
with open("orders.csv","r",encoding = "UTF8",newline = "") as f:
    orders_data = csv.DictReader(f)

    #查询表头
    print(orders_data.fieldnames)
    
    #历每一条订单并输出城市、数量、单价
    city_sales = {}
    product_sales = {}
    
    for row in orders_data:

        product = row["product"]
        city = row["city"]
        quantity = row["quantity"]
        unit_price = row["unit_price"]
        sales = order_sales(quantity, unit_price)

        print(f"商品：{product}")
        print(f"城市：{city}")
        print(f"数量:{quantity}")
        print(f"单价:{unit_price}")
        print(f"销售额为：{sales}")
        print("")
        
        #判断城市是否在列表中
        if city in city_sales:
            city_sales[city] += sales
        else:
            city_sales[city] = sales

        #判断商品是否在列表中
        if product in product_sales:
            product_sales[product] += sales
        else:
            product_sales[product] = sales

    if not city_sales:
        print("暂无订单数据，无法进行分组统计")
    else:
        print(city_sales)
        print(product_sales)

        #判断两个字典销售总额是否相等来验证统计结果
        if sum(city_sales.values()) == sum(product_sales.values()):
            print("城市与商品分组汇总总额一致，交叉验证通过")
        else:
            print("请检查订单情况")
    
