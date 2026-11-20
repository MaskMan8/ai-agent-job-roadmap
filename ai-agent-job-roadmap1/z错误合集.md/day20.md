def order_sales():
    order_sales = int(row["quantity"])*float(row["unit_price"])
    return order_sales

    不够独立，需要依赖外部环境
这个不用
def order_sales(quantity, unit_price):
    sales = int(quantity) * float(unit_price)
    return sales