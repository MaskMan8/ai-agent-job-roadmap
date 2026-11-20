阶段2：数据校验 validate_orders()
目标：找出订单数据中的问题。

完成了四项检查：
检查步骤	使用的知识	         主要功能
字段缺失	pd.isna()、strip()	检查空值和空白
重复订单	set()、in、add()	识别重复编号
数量检查	pd.to_numeric()	    检查格式和正整数规则
单价检查	pd.to_numeric()     条件判断	检查格式、负数和零价格

特别重要的是，我们区分了三种情况：
- 数据格式错误：例如 abc。
- 业务规则错误：例如数量为 -3。
- 业务待确认：例如单价为0。
这两个阶段解决了一个核心问题：

我们已经能够读取订单，并且知道每条订单是否存在问题


知识点
    1.iterrows()：遍历DataFrame
        orders_df.iterrows()
    2.pd.isna()
        pandas读取csv时候空白单元格会被认为是NaN而不是python的None，空格字符串"   "不一定会被识别为NaN
        pd.isna()作用是检查数据是否缺失
        返回True数据缺失
        返回False数据存在

    3.注意pandas中的NaN是浮点类型

    4.  quantity = "abc"
        quantity = pd.to_numeric(quantity, errors="coerce")
        结果是NaN