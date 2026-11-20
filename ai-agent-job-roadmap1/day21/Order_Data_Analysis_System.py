
import csv

# =========================
# 1. 定义必需字段
# =========================

required_fields = [
    "order_id",
    "product",
    "quantity",
    "unit_price",
    "city"
]

# =========================
# 2. 读取 CSV 并检查表头
# =========================

with open("orders.csv", "r", encoding="UTF8", newline="") as f:

    orders_data = csv.DictReader(f)

    if orders_data.fieldnames is None:
        print("订单表头缺失！")

    else:
        missing_headers = set(required_fields) - set(orders_data.fieldnames)

        if missing_headers:
            print(f"缺失必要表头：{missing_headers}")

        else:
            print("表头检查通过！")

            # =========================
            # 3. 初始化数据容器
            # =========================

            seen_order_ids = set()
            clean_orders = []
            error_logs = []
            review_orders = []
            total_orders = 0

            # =========================
            # 4. 遍历每条订单
            # =========================

            for row_number,order in enumerate(orders_data,start = 2):
                total_orders += 1

                errors = []
                review_reasons = []

                # ---------------------
                # 4.1 检查字段缺失
                # ---------------------

                for field in required_fields:

                    value = order[field]

                    if value is None or not value.strip():
                        errors.append(f"{field}字段缺失")

                # ---------------------
                # 4.2 检查重复订单
                # ---------------------

                order_id = order["order_id"]

                if order_id is not None:
                    order_id = order_id.strip()

                if order_id:
                    if order_id in seen_order_ids:
                        errors.append("订单编号重复")
                    else:
                        seen_order_ids.add(order_id)

                # ---------------------
                # 4.3 检查商品数量
                # ---------------------

                quantity = order["quantity"]

                if quantity is not None:
                    quantity = quantity.strip()

                    if quantity:
                        try:
                            quantity = int(quantity)

                            if quantity <= 0:
                                errors.append("数量必须大于0")

                        except ValueError:
                            errors.append("数量格式错误")

                # ---------------------
                # 4.4 检查商品单价
                # ---------------------

                unit_price = order["unit_price"]

                if unit_price is not None:
                    unit_price = unit_price.strip()

                    if unit_price:
                        try:
                            unit_price = float(unit_price)

                            if unit_price < 0:
                                errors.append("单价不能为负数")

                            elif unit_price == 0:
                                review_reasons.append("零价格需要业务确认")

                        except ValueError:
                            errors.append("单价格式错误")

                # ---------------------
                # 4.5 统一进行订单分类
                # ---------------------

                if errors:

                    error_log = {}
                    error_log["row_number"] = row_number
                    error_log["order_id"] = order_id
                    error_log["errors"] = errors
                    error_log["data"] = order

                    error_logs.append(error_log)

                elif review_reasons:

                    review_order = {}
                    review_order["row_number"] = row_number
                    review_order["order_id"] = order_id
                    review_order["reasons"] = review_reasons
                    review_order["data"] = order

                    review_orders.append(review_order)

                else:
                    clean_orders.append(order)

            classified_total = (
                len(clean_orders)
                + len(error_logs)
                + len(review_orders)
            )

            # =========================
            # 5. 输出检查结果
            # =========================

            print("\n===== 数据检查结果 =====")

            print(f"正常订单数量：{len(clean_orders)}")
            print(f"异常订单数量：{len(error_logs)}")
            print(f"待确认订单数量：{len(review_orders)}")
            print(f"分类后订单总数：{classified_total}")
            print(f"原始订单总数：{total_orders}")

            if total_orders == classified_total:
                print("数量核对通过")
            else:
                print("数量核对失败")

            print("\n正常订单：")
            for order in clean_orders:
                print(order)

            print("\n异常订单：")
            for error in error_logs:
                print(error)

            print("\n待确认订单：")
            for order in review_orders:
                print(order)

            # =========================
            # 6. 导出清洗后的订单 CSV
            # =========================

            try:
                with open("clean_orders.csv", "w", encoding="UTF8", newline="") as f:
                    writerfile = csv.DictWriter(f, fieldnames=required_fields)

                    writerfile.writeheader()
                    writerfile.writerows(clean_orders)
                    print("写入成功！")
            except PermissionError:
                print("文件被占用，无法写入！")

            except OSError as e:
                print("写入失败：", e)



            # =========================
            # 6. 展开异常订单数据
            # =========================

            flat_error_orders = []

            for error_log in error_logs:

                # 获取内部订单字典
                order_data = error_log["data"]

                # 创建普通字典
                flat_error = {}

                # 保存原始行号
                flat_error["row_number"] = error_log["row_number"]

                # 保存订单编号
                flat_error["order_id"] = error_log["order_id"]

                # 合并错误原因
                flat_error["errors"] = "；".join(error_log["errors"])

                # 获取内部订单数据
                flat_error["product"] = order_data["product"]
                flat_error["quantity"] = order_data["quantity"]
                flat_error["unit_price"] = order_data["unit_price"]
                flat_error["city"] = order_data["city"]

                # 保存展开后的订单
                flat_error_orders.append(flat_error)


            # =========================
            # 8. 导出异常订单 CSV
            # =========================

            error_fields = [
                "row_number",
                "order_id",
                "errors",
                "product",
                "quantity",
                "unit_price",
                "city"
            ]

            try:
                with open("error_logs.csv", "w", encoding="UTF8", newline="") as f:

                    writer = csv.DictWriter(
                        f,
                        fieldnames=error_fields
                    )

                    writer.writeheader()
                    writer.writerows(flat_error_orders)

                    print("异常订单导出成功！")

            except PermissionError:
                print("文件被占用或没有写入权限！")

            except OSError as e:
                print("异常订单导出失败：", e)


            print(f"导出异常订单数量：{len(flat_error_orders)}")


            # =========================
            # 9. 展开待确认订单
            # =========================

            flat_review_orders = []

            for review_order in review_orders:

                # 获取内部订单字典
                order_data = review_order["data"]

                # 创建普通字典
                flat_review = {}

                # 保存原始行号
                flat_review["row_number"] = review_order["row_number"]

                # 保存订单编号
                flat_review["order_id"] = review_order["order_id"]

                # 合并待确认原因
                flat_review["reasons"] = "；".join(review_order["reasons"])

                # 提取订单数据
                flat_review["product"] = order_data["product"]
                flat_review["quantity"] = order_data["quantity"]
                flat_review["unit_price"] = order_data["unit_price"]
                flat_review["city"] = order_data["city"]

                # 保存展开后的订单
                flat_review_orders.append(flat_review)


            # =========================
            # 10. 导出待确认订单 CSV
            # =========================

            review_fields = [
                "row_number",
                "order_id",
                "reasons",
                "product",
                "quantity",
                "unit_price",
                "city"
            ]

            try:
                with open("review_orders.csv", "w", encoding="UTF8", newline="") as f:

                    writer = csv.DictWriter(
                        f,
                        fieldnames=review_fields
                    )

                    writer.writeheader()
                    writer.writerows(flat_review_orders)

                    print("待确认订单导出成功！")

            except PermissionError:
                print("文件被占用或没有写入权限！")

            except OSError as e:
                print("待确认订单导出失败：", e)


            print(f"待确认订单导出数量：{len(flat_review_orders)}")
