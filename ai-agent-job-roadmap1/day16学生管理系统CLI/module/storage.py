
from pathlib import Path
import json
#决定文件位置：这样data.json就会跟着当前python走
DATA_FILE = Path(__file__).resolve().parent / "data.json"
                #__file__:当前python文件的路径
                #Path(__file__).resolve().parent：获取storsge.py所在的文件夹
                #/ "data.json"：在这个文件夹下指定data.json文件路径
#保存数据(把数据写入文件)
def save_data(students, courses, grades):
#第一步：把要保存的列表统一保存到一个字典中
    data = {
        "students": students,
        "courses": courses,
        "grades": grades
    }
#第二步：打开data.json文件
    with open(DATA_FILE, "w", encoding="utf-8") as f:
    #把Python数据写入文件(在打开的文件下面进行)
        json.dump(data,f,ensure_ascii=False,indent=4)


def load_data():
    #第一步，打开json文件
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
    #第二步，读取json文件(在打开的文件下面进行)
            data = json.load(f)
            return data["students"],data["courses"],data["grades"]
    except FileNotFoundError:
        print("首次运行，初始化空数据")
        return [],[],[]
