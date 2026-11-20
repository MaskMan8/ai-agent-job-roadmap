一、CSV是什么？
    表格数据存储格式。每一行代表一条记录，字段之间用逗号隔开。用于存放大量数据。例如把数据库里的数据导出来传给一个人要用的中间格式就是CSV。它本身就是文本格式也就是里面的数据是字符串。
    与JSON对比：
        JSON适合字典、列表和嵌套结构。
        CSV适合存储和交换结构比较规则的表格数据。
        CSV读取出来的字段一般先是字符串，后续计算数量和金额时需要类型转换。

二、CSV概念
    你需要理解三个概念：
    - 表头（Header）：第一行，描述每一列是什么。
    - 记录（Record）：一条完整的订单，例如编号为1001的订单。
    - 字段（Field）：一条记录中的单项数据，例如商品名称或单价。

三、知识点
    1.csv.DictReader：将 CSV 中的每条数据读取为字典，使用表头作为键。例如，一条订单可以通过 order["product"] 访问商品名称。字典类型的数据很容易维护。
    2.csv.DictWriter:将字典格式的数据写入 CSV 文件：字典的键对应 CSV 表头字段，字典的值对应单元格内容，无需关心列的先后顺序，自动对齐字段
    DictWriter() 有一个必要参数叫 fieldnames作用是你准备往 CSV 文件中写入哪些字段，以及字段的顺序是什么
    3..with open()：结束时自动关闭，即使读取过程中发生异常，也能更好的管理文件资源。
    4.csv.reader
      csv.writer
    5.newline="" 是 Python CSV 官方文档推荐的文件打开方式，可以避免部分环境下出现多余空行的问题。
四、读写csv文件
1.CSV读取模板：csv.reader()
import csv

try:
    with open("orders.csv", "r", encoding="utf-8", newline="") as f:
        csv_reader = csv.reader(f)

        # 读取表头
        header = next(csv_reader, None)#读取第一行表头，没有数据时返回None。
        print("表头：", header)

        # 遍历数据
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("文件不存在！")

2.CSV写入模板：csv.writer()
import csv

header = ["order_id", "product", "quantity", "unit_price", "city"]

rows = [
    ["1001", "鼠标", 2, 59, "杭州"],
    ["1002", "键盘", 1, 129, "武汉"],
    ["1003", "耳机", 3, 89, "成都"]
]

try:
    with open("orders.csv", "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)

        # 写入表头
        csv_writer.writerow(header)

        # 写入多条数据
        csv_writer.writerows(rows)

        print("写入成功！")

except PermissionError:
    print("文件被占用，无法写入！")

except OSError as e:
    print("文件写入失败：", e)

3.CSV字典读取模板：DictReader()
import csv

try:
    with open("orders.csv", "r", encoding="utf-8", newline="") as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            print(row)

            # 通过字典的键访问数据
            print("订单编号：", row["order_id"])
            print("商品名称：", row["product"])
            print("商品数量：", row["quantity"])
            print("商品单价：", row["unit_price"])
            print("所在城市：", row["city"])

except FileNotFoundError:
    print("文件不存在！")

4.CSV字典写入模板：DictWriter()
import csv

# 定义表头
fieldnames = ["order_id", "product", "quantity", "unit_price", "city"]

# 准备字典数据
rows = [
    {
        "order_id": "1001",
        "product": "鼠标",
        "quantity": 2,
        "unit_price": 59,
        "city": "杭州"
    },
    {
        "order_id": "1002",
        "product": "键盘",
        "quantity": 1,
        "unit_price": 129,
        "city": "武汉"
    }
]

try:
    with open("orders.csv", "w", encoding="utf-8", newline="") as f:

        # 创建字典写入对象，必须指定fieldnames
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)

        # 写入表头
        csv_writer.writeheader()

        # 写入多条字典数据
        csv_writer.writerows(rows)

        print("写入成功！")

except PermissionError:
    print("文件被占用，无法写入！")

except OSError as e:
    print("写入失败：", e)



    1.读取
        open中的参数设置。utf8支持全世界语言，以防止出现乱码。
        csv_reader = csv.reader(文件对象)
        csv_reader是一个可迭代的对象，一个对象就是一个行

        实际例子
            #打开文件并留存为文件句柄  instance在编程中为实例、对象
            file_instance = open("order.csv",encoding="UTF8")
            #利用reader这个模块来读取
            CSV_reader = csv.reader("file_instance")
            for line in CSV_reader
                print(line)
            file_instance.close()

    2.写入
        write_csv()
        实例：
            #打开
            #利用write模块来写入先定义header再创建写入对象
            header = ["order_id", "product", "quantity", "unit_price", "city"]
            csv_writer = csv.DictWriter(f_i, fieldnames=header)
            #正式写入代码为表头等于什么第一行是什么...
            header = ['id','product','price']
            roe_1 = ['001'，'飞机','28888']
            #如果多的话就用rows = 列表里面放列表的形式。
            CSV_writer.writeheader()
            CSV_writer.writerows(rows)
            #最后关闭

五、如果csv没有表头。
    可以用csv_reader.fielfnames检查读取对象的表头。
    例如
    if csv_reader.fieldnames is None:
    print("CSV文件为空或缺少表头")

六、为什么缺少必要的表头不能读取
    如果缺少程序无法通过预期的字段名获取数量，后续的计算就会出现错误，所有要先检查数据结构在进行业务处理，这叫数据结构校验。