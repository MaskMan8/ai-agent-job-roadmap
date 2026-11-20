import csv
import pandas as pd
from tools import load_orders, validate_orders, analyze_sales,export_results


def main():

    # 1. 读取订单
    orders_df = load_orders("orders.csv")
    # 2. 判断读取是否成功
    if orders_df is None:
        print("订单读取失败，请检查文件是否存在或格式是否正确")
        return

    print("订单读取成功")
    # 3. 校验并分类订单
    clean_orders, error_logs, review_orders = validate_orders(orders_df)
    # 4. 输出分类数量
    print(f"正常订单数量：{len(clean_orders)}")
    print(f"异常订单数量：{len(error_logs)}")
    print(f"待确认订单数量：{len(review_orders)}")

    #5.统计分析
    analysis_results = analyze_sales(clean_orders)
    print(f"总销售额：{analysis_results['total_sales']}")
    print("各城市销售额：")
    print(analysis_results["city_sales"])
    print("各商品销售额：")
    print(analysis_results["product_sales"])
    print(f"销售额最高的城市：{analysis_results['top_city']}")
    print(f"最高城市销售额：{analysis_results['max_city_sales']}")
    print(f"销售额最高的商品：{analysis_results['top_product']}")
    print(f"最高商品销售额：{analysis_results['max_product_sales']}")

    # 导出所有分析结果
    export_results(error_logs, review_orders, analysis_results)
# 程序执行入口
if __name__ == "__main__":
    main()