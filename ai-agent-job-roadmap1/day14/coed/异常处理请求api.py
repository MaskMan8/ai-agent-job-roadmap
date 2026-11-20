import requests
address = "https://jsonplaceholder.typicode.com/todos/1"
try:
    response = requests.get(address,timeout = 5)
    #检查HTTP错误
    response.raise_for_status()
    data = response.json()
    print(response.status_code)
    print(data["title"])
    if data["completed"]:
        print("任务完成")
    else:
        print("任务未完成")

#requests.exceptions.RequestException这是一个异常类型的名称，
#表示 requests 库中用于表示请求相关错误的基础异常类型
except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")

