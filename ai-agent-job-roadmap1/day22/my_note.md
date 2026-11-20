一、第一部分
Pandas把读取、清洗、筛选、聚合、合并和重塑数据等常见工作整合进一套统一api。
    优势：把原本需要手写循环或复杂数据结构操作的任务变成面向列和表格的高级操作。

Series：Pandas 的一维数据结构，可以理解为 DataFrame 中的一列

DataFrame
    有行
    有列
    有索引

知识点：
    read_csv()：它的作用是读取 CSV 文件，并将数据转换成 DataFrame。

    如何查看 DataFrame
        读取数据之后，我们通常不会立即分析，而是先检查数据。
        ① 查看数据类型：print(type(df))
        ② 查看前五行：print(df.head())
        ③ 查看数据规模:print(df.shape)
        ④ 查看所有字段名称:print(pd.columns)

    Pandas使用NaN表示缺失值的特殊标记。


二、第二部分
DataFrame的列选择与条件筛选
Pandas的常用操作之一：从大量的数据中找到我们需要的数据。
1.知识点
    以前看城市用 for order in orders:
                    print(order["city"])
    Pandas直接使用orders_df["city"]
                代码解释：orders_df:整个DataFrame
                        ["city"]选择名为city的列
        它会返回series



三、第三部分
Group By 分组统计
    作用:按照指定字段，将相同字段值的数据归到同一个组
    基本语法：df.groupby("city")

size()
    如果想知道每个组有多少行，就可以用：df.groupby("city").size()

isna()
    pandas使用它来检查缺失,它会逐行检查商品名称是否为NaN
    基本语法：df["字段"].isna()
    但是它检查不到只有空格的字符串所以要结合fillna()和strip()

fillna("")：临时把 NaN 替换为空字符串。

四、第四部分groupby+sun()销售额汇总
    1.知识点：
    1.pd.to_numeric()
        作用：用于将数据转化成数字。
        基本语法：pd.to_numeric(数据, errors="coerce")
                                    errors="coerce"的作用，遇到无法转化成数字的数据时将其转化为NaN而不是让程序报错
     注意：数字类型转换成功不代表符合业务规则
    
    2.DataFrame新增计算列
        orders_df["quantity_num"] = pd.to_numeric(
            orders_df["quantity"],
            errors="coerce"
        )
        原来的quantity保存新增quantity_num列
        df["新列"] = 数据：新增或修改列。
        pd.to_numeric()：转换数据类型

    3.drop_duplicates():Pandas 也有专门的去重方法
      基础语法：orders_df.drop_duplicates(
              subset="order_id",
              keep="first"
              )

    4.多个条件同时筛选
        一个条件的筛选
            orders_df["条件字段"] == 目标条件
        多个
            条件 = (orders_df["条件字段1"] == 目标条件1)&(orders_df["条件字段2"] == 目标条件2)&.(...)
            这个表达式生成的是一组True和False，也就是布尔Series
            需要的有条件的数据 = 临时储存数据的变量[条件]

    5.   .copy()
        作用：创建一个独立的数据副本，让我们后续修改新DataFrame时，不影响原来的DataFrame

    6.sum()
        之前valid_orders["sales"].sum()计算所有订单的销售额总和
        分组后使用groupby("city")["sales"].sum()
        则是分别计算每个城市的销售额

    7.idxmax()
        获得最大值对应的索引