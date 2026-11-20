import pandas as pd
import os

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

        row = row.to_dict()
        if errors:
            error_logs.append({"row_number": row_number, "order_id": order_id, "errors": errors,"raw_data": row })
        elif review_reasons:
            review_orders.append({"row_number": row_number, "order_id": order_id, "review_reasons": review_reasons,"raw_data": row })
        else:
            clean_orders.append(row)

    return clean_orders, error_logs, review_orders

def analyze_sales(clean_orders):
    # 定义 DataFrame 必要字段
    required_fields = [
        "order_id",
        "product",
        "quantity",
        "unit_price",
        "city"
    ]

    # 即使没有订单，也保留必要字段
    clean_df = pd.DataFrame(
        clean_orders,
        columns=required_fields
    )

    # 判断是否为空
    if clean_df.empty:

        clean_df["quantity_num"] = pd.Series(dtype="float64")
        clean_df["unit_price_num"] = pd.Series(dtype="float64")
        clean_df["sales"] = pd.Series(dtype="float64")

        city_sales = pd.Series(dtype="float64", name="sales")
        product_sales = pd.Series(dtype="float64", name="sales")

        return {
            "clean_df": clean_df,
            "total_sales": 0,
            "city_sales": city_sales,
            "product_sales": product_sales,
            "top_city": None,
            "max_city_sales": None,
            "top_product": None,
            "max_product_sales": None
        }

    # 下面保留你原来的正常订单统计代码
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

    analysis_results = {
    "clean_df": clean_df,
    "total_sales": total_sales,
    "city_sales": city_sales,
    "product_sales": product_sales,
    "top_city": top_city,
    "max_city_sales": max_city_sales,
    "top_product": top_product,
    "max_product_sales": max_product_sales
    }
    return analysis_results


def export_results(error_logs, review_orders, analysis_results):

    # 1. 创建输出文件夹
    os.makedirs("output", exist_ok=True)

    # 2. 导出正常订单
    clean_df = analysis_results["clean_df"]

    clean_df.to_csv(
        "output/clean_orders.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("正常订单导出成功！")

    # 3. 整理异常订单数据
    flat_errors = []

    for error in error_logs:

        raw_data = error["raw_data"]

        flat_error = {
            "row_number": error["row_number"],
            "order_id": error["order_id"],
            "errors": "；".join(error["errors"]),
            "product": raw_data.get("product"),
            "quantity": raw_data.get("quantity"),
            "unit_price": raw_data.get("unit_price"),
            "city": raw_data.get("city")
        }

        flat_errors.append(flat_error)

    error_df = pd.DataFrame(
        flat_errors,
        columns=[
            "row_number",
            "order_id",
            "errors",
            "product",
            "quantity",
            "unit_price",
            "city"
        ]
    )

    error_df.to_csv(
        "output/error_logs.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("异常订单导出成功！")

    # 4. 整理待确认订单数据
    flat_reviews = []

    for review in review_orders:

        raw_data = review["raw_data"]

        flat_review = {
            "row_number": review["row_number"],
            "order_id": review["order_id"],
            "review_reasons": "；".join(review["review_reasons"]),
            "product": raw_data.get("product"),
            "quantity": raw_data.get("quantity"),
            "unit_price": raw_data.get("unit_price"),
            "city": raw_data.get("city")
        }

        flat_reviews.append(flat_review)

    review_df = pd.DataFrame(
        flat_reviews,
        columns=[
            "row_number",
            "order_id",
            "review_reasons",
            "product",
            "quantity",
            "unit_price",
            "city"
        ]
    )

    review_df.to_csv(
        "output/review_orders.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("待确认订单导出成功！")

    # 5. 导出城市销售额
    city_sales = analysis_results["city_sales"]

    city_sales.rename_axis("city").rename("sales").to_csv(
        "output/city_sales.csv",
        encoding="utf-8-sig"
    )

    print("城市销售额导出成功！")

    # 6. 导出商品销售额
    product_sales = analysis_results["product_sales"]

    product_sales.rename_axis("product").rename("sales").to_csv(
        "output/product_sales.csv",
        encoding="utf-8-sig"
    )

    print("商品销售额导出成功！")

    print("\n所有分析结果导出完成！")
    print("文件保存位置：output/")