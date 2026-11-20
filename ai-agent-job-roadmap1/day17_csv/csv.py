import csv


with open("orders.csv","r",encoding = "UTF8") as f_i:
    file_instance = csv.DictReader(f_i)
    for line in file_instance:
        print(line)


#写入
with open("orders.csv","w",encoding = "UTF8") as f_i:
    header = ["order_id","product","quantity","unit_price","city"]
    csv_writer = csv.DictWriter(f_i,fieldnames=header)
    rows = [
        {"order_id": "1001",
        "product": "手枪",
        "quantity": "10",
        "unit_price": "88",
        "city": "日本"
        },
        {
        "order_id": "1002",
        "product": "飞机",
        "quantity": "2",
        "unit_price": "8888",
        "city": "美国"
        }
]
csv_writer.writeheader()
csv_writer.writerows(rows)
print("写入成功！")

