# 订单数据分析 CLI

## 项目介绍

基于 Python 和 Pandas 开发的命令行订单数据分析系统。

实现订单数据读取、数据质量检查、订单分类、
销售额统计和 CSV 结果导出。

## 核心功能

1. CSV 文件读取与必要表头检查
2. 缺失值、重复订单检查
3. 数量和单价合法性检查
4. 正常订单、异常订单、待确认订单分类
5. 按城市和商品统计销售额
6. 自动计算最高销售额城市和商品
7. 导出五类 CSV 分析结果

## 技术栈

- Python
- Pandas
- CSV
- Git

## 项目运行

在 day23 目录下执行：

python order_analysis_cli/main.py

输入文件：orders.csv

输出目录：output/

## 项目结构

order_analysis_cli/
    main.py
    tools.py
    README.md
    .gitignore

orders.csv

## 运行环境

Python 3
Pandas