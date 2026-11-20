import csv

# 必须存在的字段
required_fields = {
    "order_id",
    "product",
    "quantity",
    "unit_price",
    "city"
}

try:
    with open("orders.csv", "r", encoding="utf-8", newline="") as f_i:

        file_instance = csv.DictReader(f_i)

        # 1. 判断文件是否为空
        if file_instance.fieldnames is None:
            print("CSV文件为空，无法读取订单！")

        else:
            # 2. 获取CSV实际字段
            actual_fields = set(file_instance.fieldnames)

            # 3. 检查缺少的字段
            missing_fields = required_fields - actual_fields

            # 4. 检查多余的字段
            extra_fields = actual_fields - required_fields

            if missing_fields:
                print("缺少必要字段：", missing_fields)
                print("停止读取订单！")

            else:
                # 5. 提示多余字段
                if extra_fields:
                    print("发现多余字段：", extra_fields)

                # 6. 初始化订单计数器
                order_total = 0

                # 7. 遍历订单
                for line in file_instance:

                    order_id = line.get("order_id")
                    product = line.get("product")
                    quantity = line.get("quantity")
                    unit_price = line.get("unit_price")
                    city = line.get("city")

                    # 检查是否有缺失值
                    if any(
                        value is None or value.strip() == ""
                        for value in [
                            order_id,
                            product,
                            quantity,
                            unit_price,
                            city
                        ]
                    ):
                        print("发现数据不完整的订单，已跳过：", line)
                        continue

                    print("订单编号：", order_id)
                    print("商品：", product)
                    print("数量：", quantity)
                    print("数量的数据类型：", type(quantity))

                    print("单价：", unit_price)
                    print("单价的数据类型：", type(unit_price))

                    print("城市：", city)
                    print("--------------------")

                    # 统计有效订单数量
                    order_total += 1

                # 8. 在循环结束后输出总数
                print("有效订单总数为：", order_total)

except FileNotFoundError:
    print("订单文件不存在！")

except PermissionError:
    print("没有权限读取订单文件！")

except UnicodeDecodeError:
    print("文件编码错误！")

except csv.Error as e:
    print("CSV解析出现错误：", e)
        
