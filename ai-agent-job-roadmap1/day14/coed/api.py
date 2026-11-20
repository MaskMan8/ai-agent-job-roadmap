#请求api
#Python → requests 发送请求 → API 返回 JSON → Python 解析数据 → 打印标题

#导入python中的requests工具（）
import requests
#定义api
address = "https://jsonplaceholder.typicode.com/todos/1"
#发送get请求后服务器返回一整包东西requests将数据保存到response中
#response是“响应对象”里面打包了全部信息（包括HTTP状态码、text、content、url、header等）
response = requests.get(address)
#查看HTTP状态码，通常200表示成功
print(response.status_code)
#解析数据
data = response.json()
print(data["title"])
#判断任务状态
if data["completed"] == True:
    print("mession completed")
else:
    print("mession unfinished")