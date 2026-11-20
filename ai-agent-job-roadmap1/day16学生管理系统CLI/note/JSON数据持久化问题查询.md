一、为什么要进行JSON数据持久化？
    数据之在程序运行期间进行，退出后重新运行。

二、Python自带json模块，不需要pip install安装
    json.dump(要写入的数据，文件对象):把Python数据写入文件
    data = json.load(文件对象):从已经打开的JSON
    文件中读取数据，并转化成Python数据结构。
    它俩作用完全相反。

三、json.dump(data,f,ensure_ascii=False,indent=4)
    ensure_ascii=False：让中文在 JSON 文件中直接显示为汉字。
    indent=4：让 JSON 文件排版更整齐，方便阅读。

四、return：把读取的结果交给调用者

五、保存与加载整合
    多个变量可以同时接收函数返回多个值
    假设 load_data() 返回：
    return students, courses, grades
    那么调用：
    students, courses, grades = load_data()

六、文件路径管理问题*实际开发问题
    1.之前使用with open("data.json", "w", encoding="utf-8") as f:
    data.json是相对目录。意思是把文件保存到python当前的工作目录，而不一定是我们所需要的目录。假如你的终端之前显示过根目录，那么data.json很有可能被创建到根目录而不是我们所需的目录。

    解决方法：
        1.运行
        Get-ChildItem "D:\vscode learning python" -Filter data.json -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
        它的作用：在我的学习目录中查找data.json并显示找到文件路径。
        如果发现不在所需的文件下面先把它移动到所需文件下面。
        2.从根本上修复
            第一步：固定数据文件的位置
                在 storage.py 顶部添加
                from pathlib import Pathimport json
                DATA_FILE = Path(__file__).resolve().parent / "data.json"
                这里有一个新知识点：
                    - __file__：当前 Python 文件的路径。
                    - Path(__file__).resolve().parent：获取 storage.py 所在的文件夹。
                    - / "data.json"：在这个文件夹下指定 data.json 文件路径。
                    你不需要死记这些内容，先理解它们组合起来的目的：固定数据文件的位置。
            第二部：修改原来打开文件
                将原来打开文件中的data.json修改为DATA_FILE
七、
